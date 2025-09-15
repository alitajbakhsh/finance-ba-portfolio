# simple credit scorecard demo with logistic regression
# dataset is synthetic but logic is same as in banks

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

np.random.seed(123)
n = 1000

# fake features
income = np.random.lognormal(mean=9.7, sigma=0.5, size=n)
dti = np.clip(np.random.normal(0.35, 0.1, n), 0.01, 0.95)   # debt/income ratio
fico = np.clip(np.random.normal(690, 50, n), 500, 850)
tenor = np.random.choice([12,24,36,48,60], size=n)
amount = np.random.lognormal(mean=9.4, sigma=0.6, size=n)

# build default probs with some arbitrary formula
logit = -7 + 0.001*(680 - fico) + 1.5*(dti - 0.35)
p_default = 1/(1+np.exp(-logit))
default = np.random.binomial(1, np.clip(p_default,0.01,0.5))

df = pd.DataFrame(dict(income=income, dti=dti, fico=fico,
                       tenor=tenor, amount=amount, default=default))

X = df[["income","dti","fico","tenor","amount"]]
y = df["default"]

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_tr, y_tr)

proba = model.predict_proba(X_te)[:,1]
auc = roc_auc_score(y_te, proba)

print("AUC:", round(auc,3))

# simple risk grades by decile
te = X_te.copy()
te["pd"] = proba
te["decile"] = pd.qcut(te["pd"], 10, labels=False)+1
summary = te.groupby("decile").agg(avg_pd=("pd","mean"), n=("pd","size")).reset_index()
print(summary)
