
# 📘 Logistic Regression (Statsmodels) — Complete Beginner-Friendly Project

This repository explains Logistic Regression from absolute zero using real datasets and real code written with the **statsmodels** library.

No AI fluff. No shortcuts. Everything is explained deeply and clearly.

---

## 📂 Repository Structure

```
Logistic regression/
│
├── Admittance.csv
├── Binary predictors.csv
├── Test dataset.csv
│
├── Logistic_Regression.ipynb
├── Logistic Regression_Binary Predictors.ipynb
├── Logistic regression_manual code.ipynb
│
└── README.md
```

---

## 🧠 What Logistic Regression Actually Is

Logistic Regression is used when the output is **binary**:

- 0 or 1
- Yes or No
- True or False

It predicts **probabilities**, not raw numbers.

---

## 📊 Dataset Explanation

### Admittance.csv
Used to predict whether a student is admitted (1) or not (0).

### Binary predictors.csv
Demonstrates logistic regression using binary inputs.

### Test dataset.csv
Used to evaluate predictions on unseen data.

---

## 📘 Notebook: Logistic_Regression.ipynb

### Import Libraries
```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
```

Each library is used for:
- Math
- Data handling
- Statistical modeling

---

### Load Data
```python
data = pd.read_csv("Admittance.csv")
```

Reads the dataset into Python.

---

### Define X and y
```python
X = data[['SAT']]
y = data['Admitted']
```

X → input  
y → output

---

### Add Intercept
```python
X = sm.add_constant(X)
```

Adds β₀ to the equation.

---

### Build Model
```python
model = sm.Logit(y, X)
results = model.fit()
```

Fits logistic regression.

---

### View Summary
```python
results.summary()
```

Shows coefficients, p-values, and statistics.

---

## 📘 Binary Predictors Notebook

Shows how 0/1 inputs affect probability.

---

## 📘 Manual Logistic Regression

Explains sigmoid function and probability calculation manually.

---

## 🔢 Sigmoid Function

```
σ(z) = 1 / (1 + e⁻ᶻ)
```

Maps values to probability range.

---

## 📈 Diagram

```mermaid
graph LR
A[Linear Combination] --> B[Sigmoid Function]
B --> C[Probability]
```

---

## 🧠 Model Interpretation

- Positive coefficient → increases probability
- Negative coefficient → decreases probability
- p-value < 0.05 → significant

---

## 👨‍💻 Author
M Israr Ali
