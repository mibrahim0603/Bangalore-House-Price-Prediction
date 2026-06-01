# 🏡 Bangalore Real Estate Price Prediction Website

An end-to-end data science and machine learning project that predicts home prices in Bangalore, India based on parameters like square footage area, number of bedrooms (BHK), number of bathrooms, and location.

This project covers the entire lifecycle of a data science product: from raw data ingestion and feature engineering to building an interactive production dashboard and live deployment.

👉 **Live Streamlit Application:** [Launch Live Dashboard](https://bangalore-house-price-prediction-ckxo5pqepr94uwgyvcpud3.streamlit.app/)

---

## 🏗️ Project Architecture & Components

The application is split into two core components:
1. **Machine Learning Model:** Built using **Scikit-Learn** and **Linear Regression** on the Bangalore Home Prices dataset from Kaggle.
2. **Frontend User Interface:** A colorful, responsive web dashboard built natively with **Streamlit** that captures user inputs dynamically, structures the feature arrays, and serves real-time predictions directly using the serialized machine learning artifacts.

---

## 🛠️ Technology and Tools Used

### Data Science & Core Modeling
* **Python** (Core Language)
* **Numpy & Pandas:** Data manipulation, ingestion, structural formatting, and cleaning.
* **Matplotlib:** Statistical data visualization and checking distributions.
* **Scikit-Learn (Sklearn):** Data splitting, structural model training, and performance validation pipeline maps.
* **Jupyter Notebook:** Sandbox environment used for exploratory data analysis (EDA).

### Web UI Framework & Configuration
* **Streamlit:** Unified pythonic reactive elements (`st.slider`, `st.selectbox`, `st.button`) for frontend user input capture.
* **TOML Custom Theme:** Configures global canvas neon properties and dark palettes via a `.streamlit/config.toml` specification sheet.
* **Visual Studio Code / PyCharm:** Main Integrated Development Environments (IDEs).

---

## 💡 Data Science Concepts Covered

During the exploratory data analysis and model building phase in Jupyter Notebook, the following data science methodologies are executed sequentially:

* **Data Loading & Advanced Cleaning:** Handling missing record rows, parsing unstructured entity values (e.g., converting `"1200 - 1400"` ranges into numerical averages), and handling inconsistent string targets.
* **Feature Engineering:** Creating new metrics from existing attributes to help the linear model understand sizing densities.
* **Dimensionality Reduction:** Identifying high-cardinality categorical locations and collapsing low-frequency categorical points into an `"other"` bucket to prevent sparse matrix overhead during One-Hot Encoding.
* **Outlier Detection & Removal:** Removing operational anomalies by evaluating statistical boundaries (e.g., standard deviation techniques and business rules like minimum square feet per bedroom metrics).
* **K-Fold Cross Validation:** Ensuring model generalization stability across randomized data splits.
* **Hyperparameter Tuning via GridSearchCV:** Systematically testing multiple algorithm combinations (Linear Regression, Lasso, Decision Trees) to isolate optimal performance hyperparameters.

---

## 🚀 Installation & Local Setup

Follow these operational instructions to spin up the prediction app environment on your local machine.

### 1. Prerequisites
Ensure you have Python installed on your computer. Clone this repository and move into the project workspace:
```bash
git clone [https://github.com/mibrahim0603/Bangalore-House-Price-Prediction.git](https://github.com/mibrahim0603/Bangalore-House-Price-Prediction.git)
cd Bangalore-Real-Estate-Price-Prediction
