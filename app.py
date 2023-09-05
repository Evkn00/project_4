# Flask server
# Import necessary libraries
from flask import Flask, request, render_template, jsonify
import tensorflow as tf
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# Load the model
model = tf.keras.models.load_model('models/stroke_data_nn_model.h5')

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        if request.is_json:
            # Request contains JSON data
            data = request.get_json()  # Get JSON data as a Python dictionary
            print("Received JSON data:", data)
            print(data["gender"])

            # Preprocess
            gender = data["gender"]
            age = float(data["age"])
            hypertension = data["hypertension"]
            heart_disease = data["heart_disease"]
            ever_married = data["ever_married"]
            work_type = data["work_type"]
            residence_type = data["residence_type"]
            avg_glucose_level = float(data["avg_glucose_level"])
            smoking_status = data["smoking_status"]

            #refactor variables to put them into nn format
            #Female/Male
            gender_Female = 0
            gender_Male = 0
            gender_Other= 0


            if hypertension == "Yes":
                hypertension = 1
            else: 
                hypertension = 0

            if heart_disease == "Yes":
                heart_disease = 1
            else: 
                heart_disease = 0


            if gender == 'Female':
                gender_Female = 1

            elif gender == 'Male':
                gender_Male = 1           
            else:
                gender_Other= 1

            if ever_married == 'Yes':
                every_married_Yes = 1
                ever_married_No = 0
            else:
                every_married_Yes = 0
                ever_married_No = 1    

            #set default values for jobs
            work_type_Govt_job = 0
            work_type_Never_worked = 0
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children = 0


            if work_type == 'Private':
                work_type_Private = 1
            elif work_type == 'Self-employed':
                work_type_Self_employed = 1
            elif work_type == 'children':
                work_type_children = 1
            elif work_type == 'Never_worked':
                work_type_Never_worked = 1
            else:
                work_type_Govt_job = 1

            if residence_type == 'Urban':
                Residence_type_Rural = 0
                Residence_type_Urban = 1
            else:
                Residence_type_Rural = 1
                Residence_type_Urban = 0

            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked	= 0
            smoking_status_Unknown = 0
            smoking_status_smokes = 0



            if smoking_status == 'Smokes currently':
                smoking_status_smokes = 1
            elif smoking_status == 'Formerly smoked':
                smoking_status_formerly_smoked = 1
            elif smoking_status == 'Never smoked':
                smoking_status_formerly_smoked = 1           
            else: 
                smoking_status_Unknown = 1

#Create Numpy array from cleaned input;
        input_data = np.array([age,
                               hypertension,
                               heart_disease,
                               avg_glucose_level,
                               gender_Female,
                               gender_Male,
                               gender_Other,
                               ever_married_No,
                               every_married_Yes,
                               work_type_Govt_job,
                               work_type_Never_worked,
                               work_type_Private,
                               work_type_Self_employed,
                               work_type_children,  
                               Residence_type_Rural,
                               Residence_type_Urban,
                               smoking_status_Unknown,
                               smoking_status_formerly_smoked,
                               smoking_status_never_smoked,
                               smoking_status_smokes
])
        
        print('input_data= ', input_data)

        # Make predictions with the TF model
        prediction = model.predict(input_data.reshape(1, -1))
        print("Prediction", prediction)
        # Return predictions as JSON

        if prediction > 0.4:
            result = {'prediction': 'It is recommended that you attend the hospital immediately.',
                      'risk': 'High Risk'}
        elif prediction > 0.3:
            result = {'prediction': 'You are at risk of a stroke. It is reccomended that you see a doctor in the next few weeks for an assessment.',
                      'risk': 'Medium Risk'}
        else:
            result = {'prediction': 'You are not currently at risk of a stroke. It is however reccomended to see a doctor regularly.',
                      'risk': 'Low Risk'}

        print("result", jsonify(result['prediction']))
        return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

