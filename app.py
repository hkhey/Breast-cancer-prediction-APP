import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open(r'C:\Users\acer\Documents\M2\Cloud native & AI\NewDataset\model.pkl', 'rb'))
prediction_labels = {0: 'Benign', 1: 'Malignant'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = request.form.to_dict()
    features = list(features.values())
    features = list(map(float, features))
    final_features = np.array(features).reshape(1, 5)

    prediction = model.predict(final_features)

    predicted_label = prediction_labels[prediction[0]]

    return render_template('index.html', prediction_text='Diagnosis: {}'.format(predicted_label))

if __name__ == "__main__":
    app.run(debug=True)
