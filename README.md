
# House Price Prediction in Ames, Iowa

## Introduction

This project predicts house prices in Ames, Iowa, using a variety of features and machine learning techniques. By comparing regression models (Linear Regression and Random Forest), the project identifies the most accurate approach for predicting house prices.

The dataset used is from Kaggle's [Ames Housing Dataset](https://www.kaggle.com/datasets/marcopale/housing?select=train.csv), providing an opportunity to showcase data preprocessing, feature engineering, and model deployment.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

---

## Features

- Comprehensive **data cleaning** and **preprocessing**, including:
  - Handling missing values
  - Encoding categorical features
  - Normalization and scaling of numeric data
- **Feature engineering** to enhance prediction capabilities.
- Comparison of machine learning models:
  - **Linear Regression**
  - **Random Forest Regression**
- Deployment-ready **Flask web application** for user-friendly house price predictions.

---

## Technologies Used

- **Programming Language**: Python
- **Data Processing and Modeling**:
  - Pandas
  - NumPy
  - Scikit-learn
- **Data Visualization**:
  - Matplotlib
  - Seaborn
- **Web Development**:
  - Flask (Backend)
  - HTML and CSS (Frontend)
- **Development Environment**:
  - VS Code

---

## Prerequisites

Before starting, ensure the following are installed on your machine:

1. **Python 3.8 or higher**
   - [Download Python](https://www.python.org/downloads/)
2. **pip** (Python's package manager)
   - Check if pip is installed by running:
     ```bash
     python -m ensurepip --upgrade
     ```
3. **VS Code** (or another Python IDE)
   - [Download VS Code](https://code.visualstudio.com/)
   - Install the **Python extension** from the VS Code Marketplace.

---

## Installation

Follow these steps to set up the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/davefro/COM6033_Project_Assignment.git
   cd house-price-prediction
   ```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   Confirm the virtual environment is active: Your terminal prompt should show `(venv)` before the command line.

3. **Install dependencies**:
   Install all required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**:
   Obtain the Ames Housing dataset from Kaggle and place the dataset files in the project directory.

5. **Run the Flask application**:
   Start the Flask development server with the following command:
   ```bash
   flask run
   ```

6. **Access the application**:
   Open your web browser and go to:
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000/](http://localhost:5000/)

---

## Usage

### Prepare the Dataset:
- Ensure the dataset is placed in the project directory.
- The application automatically preprocesses the data for predictions.

### Run the Web App:
- Start the Flask server using `flask run`.
- Input house features through the web interface to get price predictions.

### Model Experimentation:
- Modify the code to experiment with different features or models.
- Evaluate performance metrics such as RMSE and R² for improvements.

---

## Contributors

- **Dawid Froncisz** - Project Developer

---

## License

This project is licensed under the [MIT License](LICENSE).
