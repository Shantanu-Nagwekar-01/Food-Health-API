# 🥗 Food Health Classifier API

This is a Flask-based REST API that classifies whether a food product is **healthy** or **unhealthy** based on its nutritional content. The classification is done using a trained **Logistic Regression** model.

---

## 📦 Features

- Accepts nutritional data as JSON input
- Returns:
  - `prediction`: `1` (Healthy) or `0` (Unhealthy)
  - `probability`: confidence scores for both classes
- Built using Flask, Scikit-learn, and Pandas
- Scales input using the same scaler used during model training

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shantanu-Nagwekar-01/Food-Health-API.git
cd Food-Health-API
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Flask server

```bash
python app.py
```

By default, it will run at `http://127.0.0.1:5000`

---

## 🌐 Live Deployment

The API is deployed and available here:
🔗 **[https://food-health-api-udsy.onrender.com](https://food-health-api-udsy.onrender.com)**

---

## 🔁 API Endpoints

### ✅ `GET /`

Test if the API is live.

**Response:**

```json
"✅ Food Health Classifier API is Live!"
```

---

### 📤 `POST /predict`

Send nutritional values in JSON format:

**Request Body Example:**

```json
{
  "Calories": 280,
  "Protein": 30,
  "Carbohydrates": 35,
  "Fat": 10,
  "Fiber": 8,
  "Sugars": 12,
  "Sodium": 250,
  "Cholesterol": 40,
  "diabetes": 0,
  "obesity": 0,
  "bp": 0
}
```

**Response Example:**

```json
{
  "prediction": 1,
  "probability": {
    "healthy": 1.0,
    "unhealthy": 0.0
  }
}
```

---

## 📁 Project Structure

```
Food-Health-API/
│
├── app.py                      # Flask app with prediction logic
├── food_classifier_mark_0.pkl # Trained Logistic Regression model
├── scaler.pkl                 # StandardScaler used for input preprocessing
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and usage
```

---

## 👨‍💻 Author

**Shantanu Nagwekar**
🔗 [GitHub Profile](https://github.com/Shantanu-Nagwekar-01)

---
