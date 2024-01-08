# Breast Cancer Diagnosis Prediction

This repository contains code for predicting breast cancer diagnosis using machine learning techniques. It includes a Jupyter Notebook for data preprocessing and model building (`Breast_cancer.ipynb`), a Flask web application for making predictions (`app.py`), and an HTML template for the web interface (`index.html`).

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Web Application](#web-application)
- Deployment on Heroku

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

## Prerequisites

- Python 3.11
- Jupyter Notebook
- Flask

You can install the required Python libraries by running:

```bash
pip install pandas scikit-learn imbalanced-learn matplotlib flask
```
### Breast_cancer.ipynb
The Breast_cancer.ipynb notebook contains the following sections:

1. Loading Data: Load the breast cancer dataset from 'Breast_cancer.csv'.
2. Checking Missing Values: Check for and handle missing values.
3. Removing Duplicates: Remove duplicate rows from the dataset.
4. Removing Unnecessary Columns: Remove columns 'id' and 'Unnamed: 32'.
5. Discovering Columns Type: Explore the data types of columns.
6. Converting 'diagnosis' Column: Convert the 'diagnosis' column to a binary variable (Malignant = 1, Benign = 0).
7. Checking Data Balance: Check the balance of classes in the target variable.
8. Performing SMOTE: Apply Synthetic Minority Over-sampling Technique (SMOTE) to balance the dataset.
9. Feature Selection (Chi-squared): Select the top 5 features using the chi-squared statistical test.
10. Model Building and Evaluation:
  10.1. Logistic Regression
  10.2. Support Vector Machine (SVM)
  10.3. Decision Trees
  10.4. k-Nearest Neighbors (KNN)
11. Saving the Best Model: Save the SVM model to 'model.pkl' for later use.
    
### app.py
The app.py script is a Flask web application that allows users to input breast cancer diagnostic features and get predictions using the trained SVM model.

1. Model Loading: Load the pre-trained SVM model from 'model.pkl'.
2. Prediction Labels: Define labels for the predictions (0 for Benign, 1 for Malignant).
3. Routes:
/: The home page with a form for user input.
/predict: The prediction route that takes user input and returns a diagnosis prediction.

### index.html
The index.html file is the HTML template for the web application. It provides a user-friendly interface with input fields for entering diagnostic features and displays the prediction result along with an image representing the diagnosis.

## Usage
1. Clone this repository to your local machine:
git clone https://github.com/your-username/breast-cancer-diagnosis.git
cd breast-cancer-diagnosis
2. Open the Jupyter Notebook (Breast_cancer.ipynb) to explore the data preprocessing and model building steps.
3. Run the Flask web application by executing the following command:
python app.py
4. Open your web browser and navigate to http://localhost:5000 to access the web interface.
Web Application
The web application allows users to input breast cancer diagnosis features and get predictions. It is a simple Flask application with an HTML front-end.

## Features
Users can input the following features for prediction:
Perimeter Mean (cm)
Area Mean (cm²)
Area SE (cm²)
Perimeter Worst (cm)
Area Worst (cm²)
The application predicts whether the diagnosis is Benign or Malignant and displays the result.
## Web Application
<div align="center">
  <img src="https://github.com/hkhey/Breast-cancer-prediction-APP/raw/main/screenshots/MainPage.PNG" alt="The Home Page" width="250" />
  <img src="https://github.com/hkhey/Breast-cancer-prediction-APP/raw/main/screenshots/predictionbenign.PNG" alt="Diagnosis Prediction Benign" width="250" />
  <img src="https://github.com/hkhey/Breast-cancer-prediction-APP/raw/main/screenshots/predictionmalignant.PNG" alt="Diagnosis Prediction Malignant" width="250" />
</div>
## Deployment on Heroku
To deploy the Breast Cancer Diagnosis Prediction app on Heroku, follow these steps:

### Create a Heroku Account:
If you don't have a Heroku account, sign up for one here.

### Install Heroku CLI:
Download and install the Heroku Command Line Interface (CLI) from here.

### Login to Heroku:
Open a terminal and run the following command to log in to your Heroku account:

heroku login
Initialize a Git Repository (if not already done):
If your project is not already a Git repository, initialize one by running:
git init
### Create a requirements.txt File:
Create a requirements.txt file in your project's root directory containing the necessary Python dependencies. You can generate this file by running:

pip freeze > requirements.txt
### Create a Procfile:
Create a file named Procfile (without any file extension) in your project's root directory with the following content:
web: python app.py
### Commit Changes to Git:
Add and commit all the changes to your Git repository:
git add .
git commit -m "Initial commit for Heroku deployment"
### Create a Heroku App:
Run the following command to create a new Heroku app:
heroku create
### Deploy to Heroku:
Push your code to the Heroku remote repository:
git push heroku master
### Open the App:
Once the deployment is successful, open the app in your browser using:
heroku open
### View Logs (Optional):
You can view the logs to check for any issues using:
heroku logs --tail
Now, your Breast Cancer Diagnosis Prediction app should be deployed on Heroku, and you can access it via the provided Heroku app URL.
<img width="960" alt="heroku" src="https://github.com/hkhey/Breast-cancer-prediction-APP/assets/76151779/29a5d6ba-8bac-4af7-9010-50ba0ed12924">

