# Deployable-Ridge-Model-using-Flask

🔥 Deployable Ridge Model using Flask

A production-ready machine learning deployment pipeline for predicting Algerian forest fire occurrences using Ridge Regression. This project demonstrates end-to-end ML deployment from Jupyter notebook experimentation to a fully functional Flask web application.

_______________________________________________________________________________

🎯 Overview
This project showcases how to deploy a machine learning model using Flask, focusing on deployment engineering rather than just model development. It bridges the gap between Jupyter notebook experimentation and production-ready web applications.
Key Highlights

Full ML Pipeline: From data preprocessing to model serving
RESTful API: Clean POST endpoint for predictions
Serialization: Proper model and scaler persistence using pickle
Web Interface: User-friendly HTML form for predictions
Production Patterns: Stateless design, preprocessing consistency

_______________________________________________________________________________

🌲 Dataset
Algerian Forest Fires Dataset
The dataset contains 244 instances covering forest fire observations from two Algerian regions:

Bejaia Region (Northeast Algeria): 122 instances
Sidi Bel-Abbes Region (Northwest Algeria): 122 instances

Time Period: June 2012 to September 2012
Features (11 attributes)
classification (fire/not fire)Integer
Target Variable: Classes (Fire: 1, Not Fire: 0)

_______________________________________________________________________________

✨ Features
🚀 Deployment Features

Flask REST API: Lightweight web framework for serving predictions
Model Serialization: Persistent model and preprocessing pipeline using pickle
Stateless Architecture: Each API call is independent
Form Data Handling: Robust input processing with type validation
Template Rendering: Dynamic HTML pages with prediction results

🤖 Machine Learning Features

Ridge Regression: L2 regularized linear regression
Feature Scaling: StandardScaler for normalization
Multi-feature Input: Handles 9 meteorological variables
Binary Classification: Fire occurrence prediction

_______________________________________________________________________________

🛠️ Installation
Prerequisites

Python 3.8 or higher
pip (Python package manager)
Virtual environment (recommended)

Step-by-Step Setup

Clone the repository

bashgit clone https://github.com/mohithnovoct/Deployable-Ridge-Model-using-Flask.git
cd Deployable-Ridge-Model-using-Flask

Create virtual environment

bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install dependencies

bashpip install -r requirements.txt
Required Packages
flask==2.3.0
numpy==1.24.3
pandas==2.0.2
scikit-learn==1.2.2
matplotlib==3.7.1
seaborn==0.12.2

🚀 Usage
1. Training the Model (Optional)
If you want to retrain the model:
bashcd notebooks
jupyter notebook Ridge_lasso_regression.ipynb
Run all cells to:

Load and preprocess data
Train Ridge Regression model
Save model and scaler as pickle files

2. Running the Flask Application
bashpython application.py
The application will start on http://0.0.0.0:8080/
3. Making Predictions
Via Web Interface

Navigate to http://localhost:8080/ in your browser
Fill in the prediction form with meteorological data:

Temperature (°C)
Relative Humidity (%)
Wind Speed (km/h)
Rainfall (mm)
FFMC, DMC, DC, ISI indices
Region (0 or 1)


Click "Submit"
View prediction result

_______________________________________________________________________________

