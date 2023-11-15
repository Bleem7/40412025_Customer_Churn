## Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

## Load the trained model
model = load_model('retrained_model.h5')

def main():
    st.title("Customer Churn App")
    st.markdown("""
        :dart: This app predicts customer churn
    """)
    st.warning("Provide customer details to predict customer churn.")

    ## Create input fields for user features
    gender = st.selectbox(' Customer gender:', ['female', 'male'])
    SeniorCitizen = st.selectbox(' Customer is a senior citizen:', [0, 1])
    Partner = st.selectbox(' Customer has partner:', ['yes', 'no'])
    PaperlessBilling = st.selectbox(' Customer has a paperlessbilling:', ['yes', 'no'])

    ## Convert categorical values to numerical values
    gender = 1 if gender == 'male' else 0
    Partner = 1 if Partner == 'yes' else 0
    PaperlessBilling = 1 if PaperlessBilling == 'yes' else 0

    ## Convert "InternetService" categorical value to numerical
    InternetService_mapping = {'DSL	': 0, 'Fiber optic': 1, 'no': 2}
    InternetService = st.selectbox('Which InternetService does customer use:', list(InternetService_mapping.keys()))
    InternetService = InternetService_mapping[InternetService]

    ## Convert "TechSupport" categorical value to numerical
    TechSupport_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    TechSupport = st.selectbox('Choose TechSupport for the customer:', list(TechSupport_mapping.keys()))
    TechSupport = TechSupport_mapping[TechSupport] 

    ## Convert "DeviceProtection" categorical value to numerical
    DeviceProtection_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    DeviceProtection = st.selectbox('Choose customer DeviceProtection:', list(DeviceProtection_mapping.keys()))
    DeviceProtection = DeviceProtection_mapping[DeviceProtection]    

    ## Convert "OnlineBackup" categorical value to numerical
    OnlineBackup_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    OnlineBackup = st.selectbox('Choose customer OnlineBackup:', list(OnlineBackup_mapping.keys()))
    OnlineBackup = OnlineBackup_mapping[OnlineBackup]

    ## Convert "MultipleLines" categorical value to numerical
    MultipleLines_mapping = {'no': 0, 'yes': 1, 'no phone service': 2}
    MultipleLines = st.selectbox('Choose the MultipleLines for the customer:', list(MultipleLines_mapping.keys()))
    MultipleLines = MultipleLines_mapping[MultipleLines]

    ## Convert "OnlineSecurity" categorical value to numerical
    OnlineSecurity_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    OnlineSecurity = st.selectbox('Choose customer online security:', list(OnlineSecurity_mapping.keys()))
    OnlineSecurity = OnlineSecurity_mapping[OnlineSecurity]

    ## Convert "PaymentMethod" categorical value to numerical
    PaymentMethod_mapping = {'Bank transfer (automatic)': 0, 'Credit card (automatic)': 1, 'Electronic check': 2, 'Mailed check':3}
    PaymentMethod = st.selectbox('Choose customer payment method:', list(PaymentMethod_mapping.keys()))
    PaymentMethod = PaymentMethod_mapping[PaymentMethod]

    ## Convert "Contract" categorical value to numerical
    contract_mapping = {'month-to-month': 0, 'one_year': 1, 'two_years': 2}
    Contract = st.selectbox('Customer has a contract:', list(contract_mapping.keys()))
    Contract = contract_mapping[Contract]
    
    tenure = st.number_input('How many months has the customer has been with the current telco provider:', min_value=0, max_value=240, value=0)
    MonthlyCharges = st.number_input('Monthly charges:', min_value=0, max_value=1000000, value=0)
    TotalCharges = tenure * MonthlyCharges

    ## Display TotalCharges
    st.warning(f'TotalCharges: {TotalCharges}')



    ##  Make prediction when the user clicks the button
    if st.button('Predict Churn'):
        prediction = model.predict([[gender, SeniorCitizen, Partner, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, PaperlessBilling, Contract, tenure, MonthlyCharges,PaymentMethod, TotalCharges]])
        predict = np.round(prediction[0],2)
        st.success(f"Customer Churn Probability: {predict}")

        # Display a message based on the churn probability (predict)
        if predict > 0.5:
            st.warning("Customer will  churn.")
        else:
            st.warning("Customer will not churn.")

        # Calculate confidence factor
        confidence_factor = 2.58 * np.sqrt((predict * (1 - predict)) / 1) 
        st.write(f"Confidence Factor: {confidence_factor}")


if __name__ == "__main__":
    main()