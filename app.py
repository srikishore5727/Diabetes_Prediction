from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model
model = joblib.load('diabetes_model.pkl')  # Make sure to use your actual model file name

# Update to match the feature names the model was trained with
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']


# Home route
# Prediction route - handle both GET and POST requests
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

        # Ensure the feature names are correct by using the proper case
        input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, 
                                    insulin, bmi, diabetes_pedigree, age]], 
                                   columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                                            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

        # Model prediction
        result = model.predict(input_data)[0]
        
        # Display result
        if result == 1:
            result = 'Diabetes detected'
        else:
            result = 'No Diabetes'

    # Return the form template with the prediction result
    return render_template('form.html', result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
