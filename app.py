from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allow all origins by default

# Load your model and scaler
model = joblib.load("./Model/food_classifier_mark_0.pkl")
scaler = joblib.load("feature_scaler.pkl")

# Define the expected features
FEATURES = ["Calories", "Protein", "Carbohydrates", "Fat", "Fiber",
            "Sugars", "Sodium", "Cholesterol", "diabetes", "obesity", "bp"]

@app.route('/', methods=['GET'])
def home():
    return "✅ Food Health Classifier API is Live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Ensure all features are present
        if not all(f in data for f in FEATURES):
            return jsonify({"error": "Missing one or more required features."}), 400

        # Convert to DataFrame
        df = pd.DataFrame([data], columns=FEATURES)

        # Scale input
        scaled_input = scaler.transform(df)

        # Make prediction
        pred = int(model.predict(scaled_input)[0])
        prob = model.predict_proba(scaled_input)[0]

        return jsonify({
            "prediction": pred,
            "probability": {
                "healthy": round(prob[1], 4),
                "unhealthy": round(prob[0], 4)
            }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
