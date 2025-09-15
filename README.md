# Finance BA Portfolio

This repo shows some small but real-world style projects for a **Business Analyst in Finance / Fintech**.  
It’s not meant to be perfect models – just clear demos of the kind of work a BA would do with data.  

---

## 📊 01 — Loan Portfolio SQL KPIs
**File:** `01-sql-kpis/loan_kpis.sql`  

- SQL queries for **delinquency buckets (30/60/90+ days past due)**  
- **Vintage default rates** by origination quarter  
- Comes with a simple schema and a couple sample inserts  

👉 This is the bread & butter of a BA in banking: writing queries, pulling metrics, explaining what they mean.

---

## 🧪 02 — A/B Testing for Conversion
**File:** `02-ab-testing/ab_test.py`  

- Simulates an experiment (control vs variant)  
- Calculates conversion rates and the difference between them  
- Runs a quick **z-test** to check if the difference is significant  

👉 This is the type of thing you’d do in fintech or digital banking when testing a new product feature.

---

## 🔐 03 — Credit Risk Scorecard
**File:** `03-credit-scorecard/credit_scorecard.py`  

- Builds a very simple **logistic regression** scorecard  
- Estimates **probability of default (PD)**  
- Prints out AUC and groups accounts into **risk deciles**  

👉 Not production-grade, but shows I understand how credit risk teams think about PD models.

---

## 🚀 Why this repo?
- Mirrors **real BA tasks**: SQL reporting, product experiment checks, working with risk data  
- Code is kept **clear & simple**, so the concepts are obvious  
- Useful in interviews to show that I can connect **business needs** with **data analysis**

---

## ▶️ How to run
- Install deps:  
  ```bash
  pip install pandas numpy scikit-learn
