# 🥗 Food Health Classifier API

This project is a **Flask-based REST API** that predicts whether a food product is **healthy** or **unhealthy** based on its nutritional content, using a trained **Logistic Regression** model.

In addition to the deployed API, this repository now contains:

* 📓 **Jupyter Notebook** (`Food_product_Classifier_mark_1.ipynb`) — complete training workflow.
* 📊 **Dataset** — nutritional information used to train the model.
* 📈 **Model Evaluation** — metrics and visualizations.

---

## 📦 Features

* Accepts nutritional data as JSON input.
* Returns:

  * `prediction`: `1` (Healthy) or `0` (Unhealthy)
  * `probability`: confidence scores for both classes.
* Built using **Flask**, **Scikit-learn**, and **Pandas**.
* Uses the same `StandardScaler` from training for preprocessing.

---

## 📊 Model Performance

* **Accuracy:** `84.15%`
* **Precision / Recall / F1-Score:**

  ```
                precision    recall  f1-score   support

       0        0.87       0.87      0.87       1204
       1        0.80       0.80      0.80        796

    accuracy                         0.84       2000
   macro avg    0.83       0.83      0.83       2000
  ```

weighted avg    0.84       0.84      0.84       2000

```

- **Confusion Matrix:**
```

\[\[1045  159]
\[ 158  638]]

```

- **ROC Curve:**
- **AUC:** `0.92`

---

## 📁 Project Structure

```

Food-Health-API/
│
├── Dataset/
│   └── daily\_food\_nutrition\_dataset.csv   # Dataset used for training
│
├── Model/
│   └── Food\_product\_Classifier\_mark\_1.ipynb  # Training & evaluation notebook
├   └── food\_classifier\_mark\_0.pkl         # Trained Logistic Regression model
│
├── app.py                             # Flask API script
├── scaler.pkl                          # StandardScaler for preprocessing
├── requirements.txt                    # Python dependencies
└── README.md                           # Project overview

````

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

By default, it runs at: `http://127.0.0.1:5000`

---

## 🌐 Live Deployment

The API is deployed here:
🔗 **[https://food-health-api-udsy.onrender.com](https://food-health-api-udsy.onrender.com)**

---

## 🔁 API Endpoints

### ✅ `GET /`

Check if API is live.
**Response:**

```json
"✅ Food Health Classifier API is Live!"
```

---

### 📤 `POST /predict`

Send nutritional data in JSON format:

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

## 👨‍💻 Author

**Shantanu Nagwekar**
🔗 [GitHub Profile](https://github.com/Shantanu-Nagwekar-01)

---
