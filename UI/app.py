
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model
model = joblib.load("/content/sample_data/best_rf_model.pkl")

# Page title
st.title(" Heart Disease Risk Predictor")

st.markdown("Enter patient health data to predict the risk of heart disease.")

# Input fields
age = st.slider("Age", 29, 77, 54)
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.slider("Resting Blood Pressure(mmHg)", 90, 200, 130)
chol = st.slider("Serum Cholesterol (mg/dl)", 100, 600, 250)
thalach = st.slider("Max Heart Rate Achieved", 70, 210, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.slider("ST depression (oldpeak)", 0.0, 6.2, 1.0)
slope = st.selectbox("Slope of ST Segment", [0, 1, 2])

# Create a DataFrame for model input
# Only include these 9 features (example)
input_data = pd.DataFrame([[age, thal, cp, trestbps, chol, thalach, exang, oldpeak, slope]],
                          columns=['age', 'thal', 'cp', 'trestbps', 'chol', 'thalach', 'exang', 'oldpeak', 'slope'])

# Prediction
if st.button("Predict Heart Disease Risk"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease! (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Low Risk of Heart Disease (Probability: {prob:.2f})")

# Optional: Upload dataset for EDA
st.markdown("---")
st.subheader("📈 Explore Heart Disease Dataset")

uploaded_file = st.file_uploader("Upload Preprocessed CSV File", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Basic stats
    st.write("### Heart Disease Distribution")
    st.bar_chart(df['target'].value_counts())

    st.write("### Age vs Cholesterol")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='age', y='chol', hue='target', palette='coolwarm', ax=ax)
    st.pyplot(fig)

    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=False, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
