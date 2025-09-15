# very simple A/B test check, not production perfect
# but shows how to compare 2 conversion rates

import numpy as np
from math import sqrt

np.random.seed(10)

# suppose control (A) has 6% conversion, variant (B) has 6.7%
nA, nB = 5000, 5000
convA, convB = 0.06, 0.067

A = np.random.binomial(1, convA, nA)
B = np.random.binomial(1, convB, nB)

pA = A.mean()
pB = B.mean()
diff = pB - pA

# pooled std error
p_pool = (A.sum() + B.sum()) / (nA + nB)
se = sqrt(p_pool*(1-p_pool)*(1/nA + 1/nB))
z = diff / se

print("Control CR:", f"{pA:.2%}")
print("Variant CR:", f"{pB:.2%}")
print("Diff:", f"{diff:.2%}")
print("z-score:", round(z,2), " -> significant if >1.96 (5% level)")
