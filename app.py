from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model files
model = joblib.load("KNN_heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    raw_input = {
        'Age': data['age'],
        'RestingBP': data['resting_bp'],
        'Cholesterol': data['cholesterol'],
        'FastingBS': data['fasting_bs'],
        'MaxHR': data['max_hr'],
        'Oldpeak': data['oldpeak'],
        'Sex_' + data['sex']: 1,
        'ChestPainType_' + data['chest_pain']: 1,
        'RestingECG_' + data['resting_ecg']: 1,
        'ExerciseAngina_' + data['exercise_angina']: 1,
        'ST_Slope_' + data['st_slope']: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    result = "High Risk of Heart Disease" if prediction == 1 else "Low Risk of Heart Disease"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
