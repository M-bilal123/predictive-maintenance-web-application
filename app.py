# import streamlit as st
# import joblib

# rfc = joblib.load('model.joblib')

# st.title("Machine Predictive Maintenance Using Random Forest")

# col_left, col_right = st.columns(2)

# # First column inputs
# with col_left:
#     type_options = ['Low', 'Medium', 'High']
#     type_mapping = {option: idx for idx, option in enumerate(type_options)}
#     selected_type = st.selectbox('Select a Type', type_options)
#     selected_type = type_mapping[selected_type]

#     process_temperature = st.text_input('Process temperature [K]')
#     torque = st.text_input('Torque [Nm]')

# # Second column inputs
# with col_right:
#     air_temperature = st.text_input('Air temperature [K]')
#     rotational_speed = st.text_input('Rotational speed [rpm]')
#     tool_wear = st.text_input('Tool wear [min]')

# # Placeholder for prediction result
# failure_pred = ''

# # Prediction button logic
# if st.button('Predict Failure'):
#     input_features = [
#         selected_type, air_temperature, 
#         process_temperature, rotational_speed, 
#         torque, tool_wear
#     ]

import streamlit as st
import joblib

# Load the model using a relative path
rfc = joblib.load('model.joblib')

st.title("Machine Predictive Maintenance Using Random Forest")

col_left, col_right = st.columns(2)

# First column inputs
with col_left:
    type_options = ['Low', 'Medium', 'High']
    type_mapping = {option: idx for idx, option in enumerate(type_options)]
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

# Prediction button logic
if st.button('Predict Failure'):
    try:
        input_features = [
            selected_type,
            float(air_temperature),
            float(process_temperature),
            float(rotational_speed),
            float(torque),
            float(tool_wear)
        ]
        
        failure_pred = rfc.predict([input_features])[0]
        failure_pred = 'Failure' if failure_pred == 1 else 'No Failure'
        st.success(failure_pred)
    
    except ValueError as e:
        st.error("Please ensure all inputs are valid numbers.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    
#     failure_pred = rfc.predict([input_features])[0]
    
#     failure_pred = 'Failure' if failure_pred == 1 else 'No Failure'
    
# st.success(failure_pred)
