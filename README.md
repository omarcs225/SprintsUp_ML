# 💓 Heart Disease Risk Prediction App

This project is a Streamlit web application that predicts the risk of heart disease based on user-provided health data using a trained Random Forest model. It also includes EDA tools for exploring uploaded datasets.

---

## 📦 Features

- ✅ Predict heart disease risk using 13 clinical parameters  
- 📊 Visualize dataset (bar charts, scatter plots, heatmaps)  
- 💻 Easy UI using Streamlit  
- 🔐 Supports deployment via Ngrok or Streamlit Cloud  

---

## 🚀 How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/heart-disease-app.git
cd heart-disease-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the Model

Ensure the trained model file `best_model_random_forest.pkl` is present in the project directory. You can train and save it like this:

```python
import joblib
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)
joblib.dump(model, "best_model_random_forest.pkl")
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Optional: Deploy on Google Colab with Ngrok

### Step 1: Set Up Environment

```bash
!pip install streamlit -q
!pip install pyngrok
```

### Step 2: Create a Simple Streamlit App (Example)

```python
%%writefile app.py
import streamlit as st

st.title('💓 Hello from Streamlit + Ngrok!')
st.write('Run Streamlit on Colab using Pyngrok.')
```

### Step 3: Deploy with Pyngrok

```python
from pyngrok import ngrok

# Set authentication token
ngrok.set_auth_token("your_ngrok_auth_token")

# Start Streamlit server
!nohup streamlit run app.py --server.port 5011 &

# Expose the port via ngrok
ngrok_tunnel = ngrok.connect(addr='5011', proto='http', bind_tls=True)

# Display the public URL
print('🔗 Public URL:', ngrok_tunnel.public_url)
```

---

## ✅ Requirements

Example `requirements.txt`:

```txt
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
pyngrok
```

---

## 📂 Project Structure

```
heart-disease-app/
├── app.py
├── best_model_random_forest.pkl
├── requirements.txt
└── README.md
```

---

## 👨‍⚕️ Input Features

- Age  
- Sex  
- Chest Pain Type (cp)  
- Resting Blood Pressure  
- Cholesterol  
- Fasting Blood Sugar  
- Resting ECG  
- Max Heart Rate  
- Exercise Induced Angina  
- ST Depression (oldpeak)  
- Slope  
- Number of Major Vessels (ca)  
- Thalassemia (thal)  

---

## 📬 Contact

Feel free to open an issue or reach out if you'd like to contribute or need support.
