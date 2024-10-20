from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
import joblib
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the trained model and vectorizers
model = tf.keras.models.load_model('symptoms_disease_model.keras')
vectorizer = joblib.load('vectorizer.pkl')
label_encoder_disease = joblib.load('label_encoder_disease.pkl')

# Load the disease information
disease_to_info = joblib.load('disease_to_info.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        symptoms = data.get('symptoms', '')

        if not symptoms:
            raise ValueError("No symptoms provided")

        # Transform the input symptoms
        X_input = vectorizer.transform([symptoms])

        # Make predictions
        disease_prediction = model.predict(X_input)
        predicted_disease_encoded = np.argmax(disease_prediction)
        predicted_disease = label_encoder_disease.inverse_transform([predicted_disease_encoded])[0]

        # Get cause and prevention
        cause = disease_to_info.get(predicted_disease, {}).get('cause', 'undefined')
        prevention = disease_to_info.get(predicted_disease, {}).get('prevention', 'undefined')

        response = {
            'disease': predicted_disease,
            'cause': cause,
            'prevention': prevention
        }
        logging.info(f"Prediction: {response}")
        return jsonify(response)
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        logging.error(f"Exception: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
