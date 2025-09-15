-- Tables are customers, loans, payments, defaults
-- this query set is kinda simplified but enough to demo BA skills

-- Delinquency buckets (30/60/90+ DPD)
WITH sched AS (
  SELECT loan_id, generate_series(0, tenor_months-1) AS m
  FROM loans
),
due AS (
  SELECT s.loan_id,
         (DATE_TRUNC('month', l.orig_date) + (s.m || ' month')::interval)::date AS due_date,
         l.amount / l.tenor_months AS due_amt
  FROM sched s
  JOIN loans l USING(loan_id)
),
paid AS (
  SELECT loan_id,
         DATE_TRUNC('month', pay_date)::date AS pay_month,
         SUM(amount) AS paid_amt
  FROM payments
  GROUP BY loan_id, DATE_TRUNC('month', pay_date)
),
agg AS (
  SELECT d.loan_id, d.due_date, d.due_amt,
         COALESCE(p.paid_amt,0) AS paid_amt
  FROM due d
  LEFT JOIN paid p
    ON p.loan_id = d.loan_id AND p.pay_month = DATE_TRUNC('month', d.due_date)
)
SELECT loan_id, due_date,
       GREATEST(0, d.due_amt - d.paid_amt) AS overdue_amt,
       CASE
         WHEN CURRENT_DATE - due_date > 90 THEN '90+'
         WHEN CURRENT_DATE - due_date > 60 THEN '60'
         WHEN CURRENT_DATE - due_date > 30 THEN '30'
         ELSE 'current'
       END AS bucket
FROM agg d
ORDER BY loan_id, due_date;

-- Default rate by vintage (quarter of origination)
WITH vint AS (
  SELECT loan_id, DATE_TRUNC('quarter', orig_date) AS vint_qtr
  FROM loans
),
stat AS (
  SELECT v.vint_qtr, COUNT(*) AS n_loans, COUNT(d.loan_id) AS n_defaults
  FROM vint v
  LEFT JOIN defaults d USING(loan_id)
  GROUP BY v.vint_qtr
)
SELECT vint_qtr, n_loans, n_defaults,
       ROUND(n_defaults::numeric / NULLIF(n_loans,0), 4) AS default_rate
FROM stat
ORDER BY vint_qtr;
