📊 Simple Linear Regression Practice — SAT vs GPA

This project demonstrates **Simple Linear Regression** using Python.  
We use SAT scores to predict students’ GPA (Grade Point Average).  
It’s a beginner-friendly example showing how regression analysis helps find relationships between two continuous variables.

---

## 🧠 What is This Project About?

The goal of this mini-project is to **understand and visualize** the relationship between a student’s SAT score and their GPA.

We use:
- **SAT** → Independent variable (input)
- **GPA** → Dependent variable (output / target)

We then build a **linear regression model** that predicts GPA based on SAT score.

---

## 🗂️ Files in This Repository

| File Name | Description |
|------------|-------------|
| `Simple_Linear_Regression_Using OLS.ipynb` | The main Jupyter Notebook with all the code, explanations, and regression analysis. |
| `Data_GPA_SAT.csv` | Dataset containing SAT and GPA values. *(You can create this CSV file from the provided data table if not already included.)* |
| `README.md` | Documentation file explaining the whole project. |

---

## 📦 Libraries Used

Make sure you have the following Python libraries installed:

```bash
pip install pandas numpy matplotlib seaborn statsmodels
```

These libraries are used for:
- **pandas** → handling the dataset  
- **numpy** → numerical operations  
- **matplotlib / seaborn** → data visualization  
- **statsmodels** → regression modeling and statistical analysis  

---

## 🧾 Dataset Description

The dataset contains two columns:

| Column | Description |
|---------|-------------|
| **SAT** | Student's SAT test score (ranging around 1600–2050) |
| **GPA** | Student's Grade Point Average (on a 4.0 scale) |

Each row represents one student’s SAT and GPA pair.  
The dataset is small and ideal for practicing **linear regression** concepts.

---

## ⚙️ How to Run the Project

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/simple-linear-regression-practice.git
   ```
2. **Navigate** into the project folder:
   ```bash
   cd simple-linear-regression-practice
   ```
3. **Open the notebook**:
   ```bash
   jupyter notebook "Simple LR Practice.ipynb"
   ```
4. **Run each cell** step by step to:
   - Load the dataset  
   - Visualize the relationship between SAT and GPA  
   - Fit the regression model  
   - Interpret the results  

---

## 📈 What the Code Does (Step-by-Step)

1. **Import Libraries**
   ```python
   import pandas as pd
   import statsmodels.api as sm
   import matplotlib.pyplot as plt
   import seaborn as sns
   ```
2. **Load Data**
   The SAT and GPA data are stored in a small dataset (either from a CSV or directly inside the notebook).

3. **Visualize Data**
   Use `sns.scatterplot()` to plot GPA vs SAT and observe the linear pattern.

4. **Build Regression Model**
   ```python
   x = sm.add_constant(x1)
   results = sm.OLS(y, x).fit()
   results.summary()
   ```
   - Adds a constant for the intercept.
   - Fits an **Ordinary Least Squares (OLS)** regression model.
   - Displays statistical summary (R², coefficients, p-values, etc.).

5. **Interpret Results**
   - **Intercept (constant)** → predicted GPA when SAT = 0  
   - **Coefficient (slope)** → how much GPA increases when SAT increases by 1 point  
   - **R-squared** → how well SAT scores explain the variation in GPA  
   - **P-value** → checks if the relationship is statistically significant  

6. **Plot Regression Line**
   Adds the best-fit line to visualize how SAT scores predict GPA.

---

## 🧩 Example Interpretation

Suppose your regression line is:

\[
GPA = 0.0017 \times SAT + 0.275
\]

This means:
- For every **1 point increase in SAT**, GPA increases by **0.0017** on average.  
- When SAT = 0, GPA would theoretically be **0.275** (though not realistic, it's part of the model).  

The **R² value** (for example, 0.40) tells us that around **40% of the variation in GPA** can be explained by SAT scores.

---

## 🎯 Learning Outcomes

By completing this project, you will learn:
- How to perform simple linear regression in Python  
- How to interpret regression summary statistics  
- How to visualize regression relationships  
- How to use `statsmodels` for OLS analysis  

---

## 🧮 Optional Improvements

You can extend this project by:
- Using a larger or real-world dataset  
- Adding more variables (e.g., study hours, attendance)  
- Using `sklearn.linear_model.LinearRegression` for comparison  
- Evaluating model performance using MSE, RMSE, and R²  

---

## 👨‍💻 Author

**M. Israr Ali**  
📍 Data Science & AI/ML Enthusiast  
📧 Feel free to connect or suggest improvements!  

---

## ⭐ Show Your Support

If you found this helpful:
- Give the repository a **star 🌟**
- Fork and try your own version
- Share feedback or open issues to improve it
