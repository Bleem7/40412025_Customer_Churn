# Customer Churn Prediction App#

## Overview##

This Streamlit app is designed for predicting customer churn based on a pre-trained machine learning model. The model takes various customer features as input and provides a probability of churn. Additionally, it calculates a confidence factor for the prediction.

# Project Structure#

Main Script: The main script is customer_churn_app.py.
Model: The trained model is loaded using TensorFlow's Keras library from the file retrained_model.h5.
Input Fields: The app provides input fields for user features such as gender, senior citizenship, partner status, and various services subscribed to by the customer.
Conversion of Categorical Values: Categorical values are converted to numerical values to be used as inputs for the machine learning model.
Prediction: When the user clicks the "Predict Churn" button, the script uses the trained model to predict the churn probability and displays the result along with a confidence factor.
User Interface: The app utilizes the Streamlit library for creating a simple and interactive user interface.

# Input Features#

Customer Gender
Senior Citizenship
Partner Status
Paperless Billing
Internet Service Type
Tech Support
Device Protection
Online Backup
Multiple Lines
Online Security
Payment Method
Contract Duration
Tenure (months with the current telco provider)
Monthly Charges
Total Charges (calculated based on tenure and monthly charges)

# Usage#

Run the script customer_churn_app.py.
Access the app in your web browser.
Input customer details in the provided fields.
Click the "Predict Churn" button to get the churn prediction and confidence factor.

# Important Notes#

The confidence factor is calculated based on the predicted churn probability.
The model assumes that the input data is in the correct format and follows the specified mappings for categorical values.

# Dependencies#

Streamlit
Pandas
NumPy
TensorFlow (for loading the pre-trained model)

# How to Install Dependencies#
pip install streamlit pandas numpy tensorflow

# How to Run the App#

streamlit run customer_churn_app.py
Feel free to customize the app based on your specific requirements and data.

# Link to video deployment#
https://1drv.ms/v/s!AkqtEjEtjHG8g19b1PeII2rn1504?e=wLBlXn
