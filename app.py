import requests
import joblib
import numpy as np
from flask import Flask, request, render_template
from io import BytesIO

app = Flask(__name__)

# GitHub raw content URL to the model file
model_url = 'https://raw.githubusercontent.com/hkhey/Breast-cancer-prediction-APP/master/model.pkl'

# Download the model file
response = requests.get(model_url)

# Check if the download was successful (status code 200)
if response.status_code == 200:
    # Load the model from the downloaded content
    model = joblib.load(BytesIO(response.content))
else:
    # Handle the case when the download fails
    print(f"Failed to download the model. Status code: {response.status_code}")
    model = None  # You can set model to None or handle it differently based on your needs

prediction_labels = {0: 'Benign', 1: 'Malignant'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text='Error: Model not available')

    features = request.form.to_dict()
    features = list(features.values())
    features = list(map(float, features))
    final_features = np.array(features).reshape(1, 5)

    prediction = model.predict(final_features)

    predicted_label = prediction_labels[prediction[0]]

    return render_template('index.html', prediction_text='Diagnosis: {}'.format(predicted_label))

if __name__ == "__main__":
    app.run(debug=True)
