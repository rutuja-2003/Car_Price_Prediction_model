# 🚗 Car Price Prediction App

A machine learning-powered Streamlit web application that predicts the resale price of a car based on key vehicle attributes such as company, model, manufacturing year, fuel type, and kilometers driven.

The application allows users to compare predictions from multiple machine learning models and evaluate their performance through key metrics such as R² Score, MAE, and RMSE. It features an interactive dashboard with a clean and user-friendly interface.

---

## 📖 Overview

The Car Price Prediction App leverages supervised machine learning algorithms to estimate the resale value of used cars. The project combines data preprocessing, model training, evaluation, and deployment using Streamlit to provide an end-to-end machine learning solution.

### Machine Learning Models Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

---

## 📂 Project Structure

```text
Car_Price_Prediction/
│
├── app.py                     # Streamlit application
├── LinearRegressionModel.pkl  # Trained Linear Regression model
├── DecisionTreeModel.pkl      # Trained Decision Tree model
├── RandomForestModel.pkl      # Trained Random Forest model
├── Cleaned_Car_data.csv       # Dataset used for training
├── requirements.txt           # Project dependencies
├── car_logo.jpg               # Logo displayed in sidebar
└── README.md                  # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Car-Price-Prediction.git
cd Car-Price-Prediction
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

After running the command, open your browser and visit:

```text
http://localhost:8501
```

---

## 🖥️ Application Features

### 🔹 Interactive Sidebar

Users can provide the following inputs:

* Car Company
* Car Model
* Manufacturing Year
* Fuel Type
* Kilometers Driven
* Machine Learning Model Selection

The model dropdown allows users to choose among:

* Linear Regression
* Decision Tree
* Random Forest

---

### 🔹 Price Prediction

After entering the required details:

* Predicts the estimated resale price of the vehicle.
* Displays the predicted price in an easy-to-read format.
* Provides a summary of all selected inputs.

---

### 🔹 Model Comparison Dashboard

Compare the performance of all trained models using:

| Metric   | Description                                           |
| -------- | ----------------------------------------------------- |
| R² Score | Measures how well the model explains variance in data |
| MAE      | Mean Absolute Error                                   |
| RMSE     | Root Mean Squared Error                               |

The dashboard presents side-by-side performance comparisons to help users understand which model performs best.

---

### 🔹 User Interface Enhancements

* Modern Streamlit layout
* Custom logo integration
* Responsive sidebar
* Navigation tabs
* Performance metric cards
* Professional dashboard design
* Footer section with project attribution

---

## 📊 Model Performance

The following models were evaluated:

### 1️⃣ Linear Regression

**Advantages**

* Simple and interpretable
* Fast training and prediction

**Limitations**

* Assumes a linear relationship between features and target variable
* Cannot effectively capture complex pricing patterns

---

### 2️⃣ Random Forest Regressor

**Advantages**

* Handles non-linear relationships
* Reduces overfitting through ensemble learning

**Limitations**

* More computationally intensive
* Did not generalize as effectively on this dataset

---

### 3️⃣ Decision Tree Regressor ⭐

**Advantages**

* Captures complex and non-linear relationships
* Easy to interpret
* Performs well on structured tabular data

**Performance Highlights**

* Highest R² Score (≈ 0.17)
* Lowest RMSE among all models
* Better representation of interactions between:

  * Company
  * Model
  * Year
  * Fuel Type
  * Kilometers Driven

### 🏆 Best Performing Model

**Decision Tree Regressor**

Based on the evaluation metrics, the Decision Tree model delivered the most reliable predictions and outperformed the other algorithms on this dataset.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib

### Machine Learning

* Linear Regression
* Decision Tree Regression
* Random Forest Regression

---

## 📌 Requirements

Recommended environment:

* Python 3.12+
* Streamlit 1.34.0
* Scikit-learn 1.4.2
* Pandas 2.2.2
* NumPy 1.26.4

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📸 Screenshots

Add screenshots of your application after deployment or local execution.

### Sidebar

```markdown
<img width="959" height="413" alt="image" src="https://github.com/user-attachments/assets/1228d9c0-c913-4dee-a010-c391119380d8" />

<img width="959" height="412" alt="image" src="https://github.com/user-attachments/assets/9f50f8d5-a21b-441b-b9b9-2166c50b7d70" />

```

### Prediction Dashboard

```markdown
![Prediction](images/prediction.png)
```

### Model Comparison

```markdown
![Comparison](images/comparison.png)
```

---

## 🚀 Future Enhancements

* Hyperparameter tuning for improved accuracy
* Additional regression models
* Feature importance visualization
* Model explainability using SHAP
* Cloud deployment (Streamlit Community Cloud / Render)
* Real-time market price integration

---

## 👩‍💻 Author

**Rutuja Kamble**

### Skills

* Python
* SQL
* Power BI
* Excel
* Machine Learning
* Data Analytics
* Data Visualization

---
