from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model
model = joblib.load('diabetes_model.pkl')  # Ensure this file is in the same folder

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route - handles both GET and POST
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    result = None

    if request.method == 'POST':
        # Get form input values
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes_pedigree'])
        age = float(request.form['age'])

        # Input data frame
        input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness,
                                    insulin, bmi, diabetes_pedigree, age]],
                                  columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                                           'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Output message
        if prediction == 1:
            result = 'Diabetes detected'
        else:
            result = 'No Diabetes'

    return render_template('index.html', result=result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
