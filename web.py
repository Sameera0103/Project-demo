import pickle  # For loading trained models
import streamlit as st  # For web app
from streamlit_option_menu import option_menu  # Sidebar menu

# Set Streamlit page configuration
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

# Load pre-trained models
diabetes_model = pickle.load(open(r"C:\Prediction of Diseases\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Prediction of Diseases\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Prediction of Diseases\parkinson_model.sav", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson’s Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# --------------------- DIABETES PREDICTION ---------------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            # Convert input values to float
            user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                             BMI, DiabetesPedigreeFunction, Age]]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = "Please enter valid numerical values for all fields."
    
    st.success(diab_diagnosis)

# --------------------- HEART DISEASE PREDICTION ---------------------
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields for heart disease (13 features)
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
        Sex = st.text_input('Sex (1 = Male, 0 = Female)')
        ChestPain = st.text_input('Chest Pain Type (0-3)')
        RestingBP = st.text_input('Resting Blood Pressure')
        Cholesterol = st.text_input('Serum Cholesterol (mg/dl)')

    with col2:
        FastingBS = st.text_input('Fasting Blood Sugar (1 = Yes, 0 = No)')
        RestingECG = st.text_input('Resting ECG Results (0-2)')
        MaxHR = st.text_input('Maximum Heart Rate Achieved')
        ExerciseAngina = st.text_input('Exercise-Induced Angina (1 = Yes, 0 = No)')

    with col3:
        Oldpeak = st.text_input('Oldpeak (ST Depression)')
        ST_Slope = st.text_input('Slope of Peak Exercise ST Segment (0-2)')
        MajorVessels = st.text_input('Number of Major Vessels (0-3)')
        Thalassemia = st.text_input('Thalassemia (0-3)')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to float
            user_input = [float(x) for x in [Age, Sex, ChestPain, RestingBP, Cholesterol, FastingBS,
                                             RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope,
                                             MajorVessels, Thalassemia]]
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        except ValueError:
            heart_diagnosis = "Please enter valid numerical values for all fields."

    st.success(heart_diagnosis)

# --------------------- PARKINSON'S PREDICTION ---------------------
elif selected == 'Parkinson’s Prediction':
    st.title("Parkinson’s Disease Prediction using ML")

    # Input fields for Parkinson's Disease (22 features)
    feature_names = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]

    # Create three-column input layout
    cols = st.columns(3)
    user_inputs = []

    for i, feature in enumerate(feature_names):
        with cols[i % 3]:  # Distribute inputs across 3 columns
            value = st.text_input(feature)
            user_inputs.append(value)

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            # Convert inputs to float
            user_input = [float(x) for x in user_inputs]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            parkinsons_diagnosis = 'The person has Parkinson’s disease' if parkinsons_prediction[0] == 1 else 'The person does not have Parkinson’s disease'
        except ValueError:
            parkinsons_diagnosis = "Please enter valid numerical values for all fields."

    st.success(parkinsons_diagnosis)
