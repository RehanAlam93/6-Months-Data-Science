# Loan Approval Prediction - EDA Project

## 📌 Project Overview
This project focuses on Exploratory Data Analysis (EDA) of a loan approval dataset. The goal is to understand patterns and relationships between different features that influence loan approval decisions.

---

## 📊 Dataset Information
The dataset contains information about applicants such as income, credit score, loan amount, years of employment, and points.

Target Variable:
- loan_approved (0 = Rejected, 1 = Approved)

---

## 🧹 Data Cleaning Steps
- Removed unnecessary columns (name, city)
- Converted target variable into numeric format
- Checked and confirmed no missing values

---

## 📈 Exploratory Data Analysis
The following visualizations were performed:
- Distribution plots (Income, Credit Score, Loan Amount, etc.)
- Box plots (feature comparison with loan approval)
- Correlation heatmap
- Pairplot for feature relationships
- Count plot for target distribution

---

## 🔑 Key Insights
- Credit score is strongly related to loan approval
- Income shows moderate influence
- Points and employment years also impact approval chances
- Loan amount has weaker direct correlation

---

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📌 Conclusion
This analysis helps in understanding the factors affecting loan approval decisions and provides a foundation for building machine learning models in the future.