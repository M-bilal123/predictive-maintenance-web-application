import streamlit as st
import joblib

rfc = joblib.load('model.joblib')

st.title("Machine Predictive Maintenance Using Random Forest")

col_left, col_right = st.columns(2)

# First column inputs
with col_left:
    type_options = ['Low', 'Medium', 'High']
    type_mapping = {option: idx for idx, option in enumerate(type_options)}
    selected_type = st.selectbox('Select a Type', type_options)
    selected_type = type_mapping[selected_type]

    process_temperature = st.text_input('Process temperature [K]')
    torque = st.text_input('Torque [Nm]')

# Second column inputs
with col_right:
    air_temperature = st.text_input('Air temperature [K]')
    rotational_speed = st.text_input('Rotational speed [rpm]')
    tool_wear = st.text_input('Tool wear [min]')

# Placeholder for prediction result
failure_pred = ''

#Prediction button logic
# Prediction button logic
if st.button('Predict Failure'):
    try:
        # Convert inputs to float, handling empty strings
        process_temperature = float(process_temperature) if process_temperature else 0.0
        torque = float(torque) if torque else 0.0
        air_temperature = float(air_temperature) if air_temperature else 0.0
        rotational_speed = float(rotational_speed) if rotational_speed else 0.0
        tool_wear = float(tool_wear) if tool_wear else 0.0

        input_features = [
            selected_type, air_temperature, 
            process_temperature, rotational_speed, 
            torque, tool_wear
        ]
        
        # Make prediction
        failure_pred = rfc.predict([input_features])[0]
        failure_pred = 'Failure' if failure_pred == 1 else 'No Failure'
        
    except ValueError as e:
        st.error(f"Invalid input: {e}")
