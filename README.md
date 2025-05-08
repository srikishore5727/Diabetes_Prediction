# 🩺 Diabetes Prediction Web App

A machine learning-based Flask web application that predicts whether a person is diabetic based on health-related inputs. This app provides a simple interface for users to get instant predictions.

## 🚀 Features

-   🔍 **Predicts diabetes** using a Random Forest Classifier.
-   📊 Trained on the **Pima Indians Diabetes Dataset**.
-   🌐 **User-friendly web interface** built with Flask and HTML.
-   ⚙️ **Real-time predictions** based on form input.
-   🧠 Utilizes a pre-trained scikit-learn model (`diabetes_model.pkl`).

---

## 🧾 Input Fields

Users need to enter the following health-related details:

-   Pregnancies (Number of times pregnant)
-   Glucose (Plasma glucose concentration a 2 hours in an oral glucose tolerance test)
-   Blood Pressure (Diastolic blood pressure - mm Hg)
-   Skin Thickness (Triceps skin fold thickness - mm)
-   Insulin (2-Hour serum insulin - mu U/ml)
-   BMI (Body mass index - weight in kg/(height in m)^2)
-   Diabetes Pedigree Function (A function that scores likelihood of diabetes based on family history)
-   Age (Age in years)

⚠️ **Important:** All input values must be numeric.

---

## 📁 Project Structure

```
    diabetes_prediction/
    │
    ├── app.py                 # Flask application
    ├── diabetes_model.pkl     # Trained ML model 
    ├── requirements.txt       # Python dependencies
    ├── templates/
        └── form.html        # HTML form for user input

```



---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
*   Python (3.7+ recommended)
*   pip (Python package installer)

---

## 🧪 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/srikishore5727/Diabetes_Prediction.git
    cd Diabetes_Prediction
    ```

2.  **Create and activate a virtual environment** (optional but highly recommended):
    *   On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the Flask application:**
    ```bash
    python app.py
    ```

5.  **Open your web browser** and navigate to:
    ```
    http://127.0.0.1:5000
    ```

---

## 📦 Notes About the Model (`diabetes_model.pkl`)

-   `diabetes_model.pkl` is a binary file containing the serialized, pre-trained Random Forest Classifier model from `scikit-learn`.
-   It is not human-readable in plain text (e.g., on GitHub) but is loaded by the Python script (`app.py`) to make predictions.
-   The model was trained on the Pima Indians Diabetes Dataset to predict the onset of diabetes.

---


![App Screenshot](https://res.cloudinary.com/dpgmbfxsz/image/upload/v1746725005/gxr0g09sgwgh96vpyas9.png)

---

## 👨‍💻 Developed by

Sri Kishore ([@srikishore5727](https://github.com/srikishore5727))