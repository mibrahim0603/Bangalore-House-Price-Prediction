# 🏡 Bangalore Real Estate Price Prediction Website

An end-to-end data science and machine learning project that predicts home prices in Bangalore, India based on parameters like square footage area, number of bedrooms (BHK), number of bathrooms, and location.

This project covers the entire lifecycle of a data science product: from raw data ingestion and feature engineering to building an HTTP production server and deployment of a lightweight user interface.

---

## 🏗️ Project Architecture & Components

The application is split into three core components:
1. **Machine Learning Model:** Built using **Scikit-Learn** and **Linear Regression** on the Bangalore Home Prices dataset from Kaggle.
2. **Backend Production Server:** A **Python Flask** server that exposes a REST API endpoint (`/predict_home_price`) to serve real-time HTTP pricing requests using the serialized machine learning artifacts.
3. **Frontend Client Interface:** A clean web application built using standard **HTML, CSS, and JavaScript (jQuery)** that accepts user configurations and communicates asynchronously with the Flask application layer.

---

## 🛠️ Technology and Tools Used

### Data Science & Core Modeling
* **Python** (Core Language)
* **Numpy & Pandas:** Data manipulation, ingestion, structural formatting, and cleaning.
* **Matplotlib:** Statistical data visualization and checking distributions.
* **Scikit-Learn (Sklearn):** Data splitting, structural model training, and performance validation pipeline maps.
* **Jupyter Notebook:** Sandbox environment used for exploratory data analysis (EDA).

### Backend Server & Web UI
* **Python Flask:** Routing server layer framework handling API traffic vectors.
* **HTML / CSS / JavaScript:** User responsive data entry cards, layout styling, and DOM manipulation.
* **jQuery:** Handles asynchronous background network communication (`$.post` AJAX streams).
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
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd Bangalore-Real-Estate-Price-Prediction

2. Run the Python Flask Server

Navigate to your server directory folder framework, install the tracking package dependencies, and run the entry script:
Bash

# Navigate to the server folder
cd server

# Install the necessary library requirements
pip install flask numpy pandas scikit-learn

# Launch the backend API process
python server.py

The server will initialize, load the trained artifacts (bangalore_home_prices_model.pickle and columns.json), and start listening for data inquiries on port http://127.0.0.1:5000/.
3. Open the Frontend Interface

Because standard modern browsers block cross-origin requests when running via local directory layouts, use a dedicated web viewer to host the UI folder layout safely:

    Open the project's client folder inside VS Code.

    Click the "Go Live" ribbon icon at the bottom of the editor pane to launch the Live Server extension.

    Access your web UI layout interface dashboard link via: http://127.0.0.1:5500/app.html

Input the square footage, bedrooms, and location to see your trained predictive pipeline calculate real estate estimations in real-time!