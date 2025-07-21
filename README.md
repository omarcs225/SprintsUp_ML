# 💓 Heart Disease Risk Prediction App

This project is a Streamlit web application that predicts the risk of heart disease based on user-provided health data using a trained Random Forest model. It also includes EDA tools for exploring uploaded datasets.

---

## 📦 Features

✅ Predict heart disease risk using 13 clinical parameters 
📊 Visualize dataset (bar charts, scatter plots, heatmaps)  
💻 Easy UI using Streamlit  
🔐 Supports deployment via Ngrok or Streamlit Cloud  

---

## 🚀 How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/heart-disease-app.git
cd heart-disease-app
```
###2. Install Dependencies
pip install -r requirements.txt

### 3. Add the Model
Ensure the trained model file best_model_random_forest.pkl is present in the project directory. You can train and save it like this:
```bash
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
## 🌐 Optional: Deploying platforms like Google Colab

###  Step 1: Setting Up Environment
First things first, let’s install Streamlit and Pyngrok.
```bash
!pip install streamlit -q
!pip install pyngrok
```

### Step 2: Crafting Your Streamlit App
Now, let your creativity shine by crafting a captivating Streamlit application. For demonstration purposes, we’ll create a simple “Hello World” app.

```bash
%%writefile app.py
import streamlit as st

st.write('# Hello World from ypred, please subscribe')
st.write('## Run Streamlit on Colab with `pyngrok` ')
```
### Step 3: Deploying with Pyngrok Magic
It’s showtime! Let’s deploy our Streamlit app using Pyngrok’s magic.
```bash
from pyngrok import ngrok

# Set authentication token if you haven't already done so
ngrok.set_auth_token("your_ngrok_auth_token")

# Start Streamlit server on a specific port
!nohup streamlit run app.py --server.port 5011 &

# Start ngrok tunnel to expose the Streamlit server
ngrok_tunnel = ngrok.connect(addr='5011', proto='http', bind_tls=True)

# Print the URL of the ngrok tunnel
print(' * Tunnel URL:', ngrok_tunnel.public_url)
```
## Now, go ahead and dazzle the world with your incredible machine-learning models!
