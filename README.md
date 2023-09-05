# Stroke Data Set Machine Learning Project
## 1. Project Goal:
To create a machine learning model that can predict with over 75% accuracy whether a patient is likely to have a stroke based on a series of medical statistics. I will then use the machine learning model to create a web app that will allow a user to enter statistics and have a risk level of Low, Medium or High returned. We will try at least two different learning models until we can reach or exceed the target accuracy. 

## 2. The Dataset
We will be using the Stroke prediction data set by user Fedesoriano from Kaggle. The dataset can be found here: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/code

There are 5100 observations with 12 features each in this data set. The features are:
1) id: unique identifier
2) gender: "Male", "Female" or "Other"
3) age: age of the patient
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6) ever_married: "No" or "Yes"
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8) Residence_type: "Rural" or "Urban"
9) avg_glucose_level: average glucose level in blood
10) bmi: body mass index
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
12) stroke: 1 if the patient had a stroke or 0 if not. This will be the target variable for the ML models.

## 4. Data Analysis
I decided to use the ydata_profile package for automated EDA for this project. The package provides detailed EDA with a single line of code. The automated EDA then lead to some extra manual examiniation using Seaborn and Pandas. 

## 5. Data Cleaning
Initially the id feature was dropped from the dataset as it was not relevant for the ML models.

### Bmi
BMI is the only feature in the dataset with any missing values. A large number (40 of 202) of the missing values were on rows that had stroke = 1, which meant that around 25% of our rows with a positive target had BMI missing. The correlation of BMI to the target variable was also weak, possibly due to the missing values. I ran a version of the first machine learning model with BMI using the missing values replaced with the mean BMI, but it did not perform any better or worse than the model if BMI was excluded, so BMI was excluded from the dataset. 

![image](https://github.com/Evkn00/project_4/assets/69624124/79a29753-fb67-4013-b904-23218e4ea924)

![image](https://github.com/Evkn00/project_4/assets/69624124/dece073c-7ece-49ec-94c7-661eab097da9)

### Skewed data set.
Only 202 of over 5000 of the observations had a positive target variable. However this did not seem to effect the model's ability to accurately predict after a reasonble amount of testing. However this is something that likely could benefit from something like SMOTE (Synthetic Minority Oversampling Technique) at a later date.

### Outliers
BMI will be ignored as it is not included in the data set, which only leaves avg_glucose_level showing any possible outliers, however looking at a scatter most of the positive target variables have an avg_glucose_level that would put them outside of the 3rd quartile, which shows that the correlation of avg_glucose_level to stroke = 1 is very strong. No outliers will be removed.
![image](https://github.com/Evkn00/project_4/assets/69624124/d793b833-ce60-4c2b-9341-ad007683aa65)
![image](https://github.com/Evkn00/project_4/assets/69624124/fd84a903-e3b7-45a8-91c2-bbb01eb85ce3)
![image](https://github.com/Evkn00/project_4/assets/69624124/9954dae8-8ea9-4de3-bf25-4ecd13164447)

## 5. Machine Learning Models
Only two machine learning models were attempted as the results of both far exceeded the target (75% accuracy).

### Decision Tree
Using the SKLEARN RandomForestClassifier model an accuracy of 95% was achieved. 
![image](https://github.com/Evkn00/project_4/assets/69624124/7753d7b7-4f8d-4e2a-a4ab-2538e0230edc)
Hyperparamater tuning was attempted, however there was almost no improvement after a considerable attempt. 
![image](https://github.com/Evkn00/project_4/assets/69624124/d8bc7a35-c216-4f6b-b7ff-c0f33c28c3ad)

### Tensorflow Neural Netowrk
The initial attempt with default parameters achieved 94.81% accuracy, and after over 500 runs of attempted hyperparameter tuning an oncease of around 0.5% was achieved. 
![image](https://github.com/Evkn00/project_4/assets/69624124/af6df0e1-27a5-480f-9c5f-e23d648075b3)
``` json
#Best performing parameters
{'activation': 'relu',
 'first_units': 91,
 'num_layers': 1,
 'units_0': 81,
 'units_1': 11,
 'units_2': 21,
 'units_3': 21,
 'units_4': 1,
 'units_5': 21,
 'tuner/epochs': 100,
 'tuner/initial_epoch': 0,
 'tuner/bracket': 0,
 'tuner/round': 0}
```

This model was selected for use in the Webapp as it was slightly more accurate.

## 6. The Webapp
The web app was created using a python flask API accepting inputs from a HTML page and then runing the model predictions based on the submitted data and then returning a value to the Webapp. Risk levels were assigned based on the Sigmoid number returned by the model:
  #### High Risk: >0.4
  #### Medium Risk: >0.3
  #### Low Risk: <0.3

## 7. Files

app.py - flask API for serving the ML model. 
stroke_data_EDA.ipynb - EDA of dataset
storke_data_decision_Tree.ipynb - Decision tree modeling
stroke_data_nn.ipynb - Neural Network modeling
templates/index.html - main webapp html file
models/stroke_data_nn_model.h5 - Neural network model for flask API. 
resources/healthcare-dataset-stroke-data.csv - dataset for project







