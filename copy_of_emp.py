# -*- coding: utf-8 -*-
"""Copy of emp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ygzo54XHvIEnNeIr4X0NWJXVjtyoi41m
"""

import pandas as pd

data=pd.read_csv("/content/adult 3.csv")

data.head(10)

data.tail(3)

data.shape

#null values
data.isna().sum() #mean mdeian mode arbitrary

print(data.workclass.value_counts())

data.workclass.replace({'?':'Others'},inplace=True)
print(data['workclass'].value_counts())

print(data['occupation'].value_counts())

data.occupation.replace({'?':'Others'},inplace=True)
print(data['occupation'].value_counts())

data=data[data['workclass']!='Without-pay']
data=data[data['workclass']!='Never-worked']
print(data['workclass'].value_counts())

print(data.relationship.value_counts())

print(data.gender.value_counts())

data.shape

#outlier detection
import matplotlib.pyplot as plt   #visualization
plt.boxplot(data['age'])
plt.show()

data=data[(data['age']<=75)&(data['age']>=17)]

plt.boxplot(data['age'])
plt.show()

data.shape

plt.boxplot(data['capital-gain'])
plt.show()

plt.boxplot(data['capital-gain'])
plt.show()

plt.boxplot(data['educational-num'])
plt.show()

data=data[(data['educational-num']<=16)&(data['educational-num']>=5)]

plt.boxplot(data['educational-num'])
plt.show()

plt.boxplot(data['hours-per-week'])
plt.show()

data.shape

data=data.drop(columns=['education']) #redundant features removal

data

from sklearn.preprocessing import LabelEncoder   #import libarary
encoder=LabelEncoder()                       #create object
data['workclass']=encoder.fit_transform(data['workclass']) #7 categories   0,1, 2, 3, 4, 5, 6,
data['marital-status']=encoder.fit_transform(data['marital-status'])   #3 categories 0, 1, 2
data['occupation']=encoder.fit_transform(data['occupation'])
data['relationship']=encoder.fit_transform(data['relationship'])      #5 categories  0, 1, 2, 3, 4
data['race']=encoder.fit_transform(data['race'])
data['gender']=encoder.fit_transform(data['gender'])    #2 catogories     0, 1
data['native-country']=encoder.fit_transform(data['native-country'])

data

x=data.drop(columns=['income'])
y=data['income']
x

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, OneHotEncoder

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

models = {
    "LogisticRegression": LogisticRegression(),
    "RandomForest": RandomForestClassifier(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "GradientBoosting": GradientBoostingClassifier()
}

results = {}

for name, model in models.items():
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"{name} Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt
plt.bar(results.keys(), results.values(), color='skyblue')
plt.ylabel('Accuracy Score')
plt.title('Model Comparison')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Define models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "GradientBoosting": GradientBoostingClassifier()
}

results = {}

# Train and evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    results[name] = acc
    print(f"{name}: {acc:.4f}")

# Get best model
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
print(f"\n✅ Best model: {best_model_name} with accuracy {results[best_model_name]:.4f}")

# Save the best model in the 'model' directory
if not os.path.exists('model'):
    os.makedirs('model')
joblib.dump(best_model, "model/best_model.pkl")
print("✅ Saved best model as model/best_model.pkl")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import joblib
# import numpy as np
# import base64 # Import the base64 module
# import os # Import the os module
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# # Load the trained model
# try:
#     model = joblib.load("model/best_model.pkl")
# except Exception as e:
#     st.error(f"Error loading model: {str(e)}")
#     st.error("This may be due to a scikit-learn version compatibility issue.")
#     st.info(
#         "Please check that the model was trained with a compatible scikit-learn version."
#     )
#     st.stop()
# 
# # Define label encoding mappings based on the original dataset
# # Get the unique native countries from the data used for training
# try:
#     # This assumes 'data' DataFrame is available in the environment where this script is run
#     # In a real deployment, you would likely load these from a config or the original data source
#     NATIVE_COUNTRY_MAPPING = {country: i for i, country in enumerate(sorted(pd.read_csv("/content/adult 3.csv")['native-country'].unique()))}
#     # Sort the dictionary by keys to maintain consistent order in the selectbox
#     NATIVE_COUNTRY_MAPPING = dict(sorted(NATIVE_COUNTRY_MAPPING.items()))
# except Exception as e:
#     st.error(f"Error loading native country mapping: {str(e)}")
#     # Fallback mapping if loading from data fails
#     NATIVE_COUNTRY_MAPPING = {
#         "United-States": 39, "Cambodia": 4, "England": 10, "Puerto-Rico": 32, "Canada": 5,
#         "Germany": 13, "Outlying-US(Guam-USVI-etc)": 26, "India": 17, "Japan": 19, "Greece": 14,
#         "South": 36, "China": 6, "Cuba": 7, "Iran": 18, "Honduras": 15, "Philippines": 31,
#         "Italy": 20, "Poland": 30, "Jamaica": 21, "Vietnam": 40, "Mexico": 25, "Portugal": 33,
#         "Ireland": 22, "France": 12, "Dominican-Republic": 9, "Laos": 23, "Ecuador": 8,
#         "Taiwan": 37, "Haiti": 16, "Columbia": 34, "Hungary": 35, "Guatemala": 38,
#         "Nicaragua": 28, "Scotland": 29, "Thailand": 24, "Yugoslavia": 41, "El-Salvador": 11,
#         "Trinadad&Tobago": 27, "Peru": 3, "Hong": 2, "Holand-Netherlands": 1, "?": 0,
#     }
# 
# 
# WORKCLASS_MAPPING = {
#     "Private": 4,
#     "Self-emp-not-inc": 6,
#     "Self-emp-inc": 5,
#     "Federal-gov": 1,
#     "Local-gov": 2,
#     "State-gov": 7,
#     "Without-pay": 8,
#     "Never-worked": 3,
#     "?": 0,
#     "Others": 0 # Add 'Others' mapping to handle replaced values
# }
# 
# MARITAL_STATUS_MAPPING = {
#     "Married-civ-spouse": 2,
#     "Divorced": 0,
#     "Never-married": 4,
#     "Separated": 5,
#     "Widowed": 6,
#     "Married-spouse-absent": 3,
#     "Married-AF-spouse": 1,
# }
# 
# OCCUPATION_MAPPING = {
#     "Tech-support": 13,
#     "Craft-repair": 2,
#     "Other-service": 7,
#     "Sales": 11,
#     "Exec-managerial": 3,
#     "Prof-specialty": 10,
#     "Handlers-cleaners": 5,
#     "Machine-op-inspct": 6,
#     "Adm-clerical": 0,
#     "Farming-fishing": 4,
#     "Transport-moving": 14,
#     "Priv-house-serv": 9,
#     "Protective-serv": 8,
#     "Armed-Forces": 1,
#     "?": 12,
#     "Others": 12 # Add 'Others' mapping to handle replaced values
# }
# 
# RELATIONSHIP_MAPPING = {
#     "Wife": 5,
#     "Own-child": 3,
#     "Husband": 0,
#     "Not-in-family": 1,
#     "Other-relative": 2,
#     "Unmarried": 4,
# }
# 
# RACE_MAPPING = {
#     "White": 4,
#     "Asian-Pac-Islander": 1,
#     "Amer-Indian-Eskimo": 0,
#     "Other": 3,
#     "Black": 2,
# }
# 
# GENDER_MAPPING = {"Male": 1, "Female": 0}
# 
# 
# EDUCATION_NUM_MAPPING = {
#     "Preschool": 1,
#     "1st-4th": 2,
#     "5th-6th": 3,
#     "7th-8th": 4,
#     "9th": 5,
#     "10th": 6,
#     "11th": 7,
#     "12th": 8,
#     "HS-grad": 9,
#     "Some-college": 10,
#     "Assoc-voc": 11,
#     "Assoc-acdm": 12,
#     "Bachelors": 13,
#     "Masters": 14,
#     "Prof-school": 15,
#     "Doctorate": 16,
# }
# 
# st.set_page_config(
#     page_title="Employee Salary Prediction",
#     page_icon="💼",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
# 
# # Custom CSS for a dark style background with bright elements
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()
# 
# img_file_path = "/content/rp.jpg"
# img_base64 = None
# 
# if os.path.exists(img_file_path):
#     try:
#         img_base64 = get_base64_of_bin_file(img_file_path)
#     except Exception as e:
#         st.warning(f"Could not load background image: {e}")
# 
# background_css = """
# <style>
#     .stApp {
#         background-color: #1e1e1e; /* Default dark background */
#         color: #f8f8f2; /* Light text color */
#     }
#     .main-header {
#         text-align: center;
#         background: linear-gradient(90deg, #ff7e5f 0%, #feb47b 100%); /* Bright gradient for the header */
#         padding: 2rem;
#         border-radius: 10px;
#         margin-bottom: 2rem;
#         color: white; /* White text for contrast */
#         border: 2px solid white; /* White border for the main header */
#     }
#     .metric-card {
#         background: #2d2d2d; /* Slightly lighter dark for cards */
#         padding: 1rem;
#         border-radius: 10px;
#         border: 1px solid #444; /* Add a subtle border */
#         border-left: 4px solid #a8e6cf; /* Bright accent color */
#         margin: 0.5rem 0;
#         color: #f8f8f2; /* Light text */
#     }
#     /* Ensure metric labels and values are visible */
#     [data-testid="stMetricLabel"] div {
#         color: #f8f8f2 !important; /* Light color for metric labels */
#     }
#     [data-testid="stMetricValue"] {
#         color: #a8e6cf !important; /* Bright color for metric values */
#     }
# 
#     .prediction-success {
#         background: linear-gradient(90deg, #56ab2f 0%, #a8e6cf 100%);
#         padding: 1rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         font-size: 1.2rem;
#         font-weight: bold;
#     }
#     .prediction-error {
#         background: linear-gradient(90deg, #ff416c 0%, #ff4b2b 100%);
#         padding: 1rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#     }
#     .sidebar .sidebar-content {
#         background: #2d2d2d; /* Dark sidebar background */
#         color: #f8f8f2; /* Light text */
#     }
#     .sidebar .sidebar-content .markdown-text-container {
#         color: #f8f8f2; /* Ensure markdown text in sidebar is light */
#     }
#     .stButton > button {
#         background: linear-gradient(90deg, #a8e6cf 0%, #dcedc1 100%); /* Bright button gradient */
#         color: #1e1e1e; /* Dark text for contrast */
#         border: none;
#         padding: 0.5rem 2rem;
#         border-radius: 25px;
#         font-weight: bold;
#         transition: all 0.3s;
#     }
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 5px 15px rgba(168, 230, 207, 0.4); /* Shadow matching bright color */
#     }
#     /* Ensure text in expanders is light */
#     .streamlit-expanderHeader {
#         color: #f8f8f2 !important;
#     }
#     .streamlit-expanderContent .markdown-text-container {
#         color: #f8f8f2 !important;
#     }
#     /* Adjust selectbox text color in sidebar */
#     .stSidebar .stSelectbox div[data-baseweb="select"] div {
#         color: #000000 !important; /* Set text color to black */
#     }
#      /* Adjust number input text color in sidebar */
#     .stSidebar .stNumberInput input {
#         color: #000000 !important; /* Set text color to black */
#     }
#      /* Adjust slider text color in sidebar */
#     .stSidebar .stSlider [data-testid="stTickBarMin"],
#     .stSidebar .stSlider [data-testid="stTickBarMax"],
#     .stSidebar .stSlider [data-testid="stThumbValue"] {
#         color: #000000 !important; /* Set text color to black */
#     }
#     .stSlider [data-testid="stTrack"] {
#         background: #3d3d3d; /* Darker track */
#     }
#     .stSlider [data-testid="stThumb"] {
#         background: #a8e6cf; /* Bright thumb */
#     }
#     /* Ensure general sidebar text is visible */
#     .stSidebar .css-1lcbmhc, .stSidebar .css-1adrxjp { /* Selectors for sidebar text elements */
#         color: #f8f8f2 !important; /* Set text color to light */
#     }
#     /* Add white border to all boxes on the right side */
#     .block-container { /* This is a general container, might need refinement */
#         border: 1px solid white !important;
#         border-radius: 5px; /* Optional: add some rounding */
#         padding: 10px; /* Optional: add some padding inside the border */
#         margin-bottom: 10px; /* Optional: add some space between blocks */
#     }
# </style>
# """
# 
# if img_base64:
#     background_css = f"""
# <style>
#     .stApp {{
#         background-image: url('data:image/jpeg;base64,{img_base64}');
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed; /* Keeps background fixed when scrolling */
#         color: #f8f8f2; /* Light text color */
#     }}
#     .main-header {{
#         text-align: center;
#         background: linear-gradient(90deg, #ff7e5f 0%, #feb47b 100%); /* Bright gradient for the header */
#         padding: 2rem;
#         border-radius: 10px;
#         margin-bottom: 2rem;
#         color: white; /* White text for contrast */
#         border: 2px solid white; /* White border for the main header */
#     }}
#     .metric-card {{
#         background: #2d2d2d; /* Slightly lighter dark for cards */
#         padding: 1rem;
#         border-radius: 10px;
#         border: 1px solid #444; /* Add a subtle border */
#         border-left: 4px solid #a8e6cf; /* Bright accent color */
#         margin: 0.5rem 0;
#         color: #f8f8f2; /* Light text */
#     }}
#     /* Ensure metric labels and values are visible */
#     [data-testid="stMetricLabel"] div {{
#         color: #f8f8f2 !important; /* Light color for metric labels */
#     }}
#     [data-testid="stMetricValue"] {{
#         color: #a8e6cf !important; /* Bright color for metric values */
#     }}
# 
#     .prediction-success {{
#         background: linear-gradient(90deg, #56ab2f 0%, #a8e6cf 100%);
#         padding: 1rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         font-size: 1.2rem;
#         font-weight: bold;
#     }}
#     .prediction-error {{
#         background: linear-gradient(90deg, #ff416c 0%, #ff4b2b 100%);
#         padding: 1rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#     }}
#     .sidebar .sidebar-content {{
#         background: #2d2d2d; /* Dark sidebar background */
#         color: #f8f8f2; /* Light text */
#     }}
#     .sidebar .sidebar-content .markdown-text-container {{
#         color: #f8f8f2; /* Ensure markdown text in sidebar is light */
#     }}
#     .stButton > button {{
#         background: linear-gradient(90deg, #a8e6cf 0%, #dcedc1 100%); /* Bright button gradient */
#         color: #1e1e1e; /* Dark text for contrast */
#         border: none;
#         padding: 0.5rem 2rem;
#         border-radius: 25px;
#         font-weight: bold;
#         transition: all 0.3s;
#     }}
#     .stButton > button:hover {{
#         transform: translateY(-2px);
#         box-shadow: 0 5px 15px rgba(168, 230, 207, 0.4); /* Shadow matching bright color */
#     }}
#     /* Ensure text in expanders is light */
#     .streamlit-expanderHeader {{
#         color: #f8f8f2 !important;
#     }}
#     .streamlit-expanderContent .markdown-text-container {{
#         color: #f8f8f2 !important;
#     }}
#     /* Adjust selectbox text color in sidebar */
#     .stSidebar .stSelectbox div[data-baseweb="select"] div {{
#         color: #000000 !important; /* Set text color to black */
#     }}
#      /* Adjust number input text color in sidebar */
#     .stSidebar .stNumberInput input {{
#         color: #000000 !important; /* Set text color to black */
#     }}
#      /* Adjust slider text color in sidebar */
#     .stSidebar .stSlider [data-testid="stTickBarMin"],
#     .stSidebar .stSlider [data-testid="stTickBarMax"],
#     .stSidebar .stSlider [data-testid="stThumbValue"] {{
#         color: #000000 !important; /* Set text color to black */
#     }}
#     .stSlider [data-testid="stTrack"] {{
#         background: #3d3d3d; /* Darker track */
#     }}
#     .stSlider [data-testid="stThumb"] {{
#         background: #a8e6cf; /* Bright thumb */
#     }}
#     /* Ensure general sidebar text is visible */
#     .stSidebar .css-1lcbmhc, .stSidebar .css-1adrxjp {{ /* Selectors for sidebar text elements */
#         color: #f8f8f2 !important; /* Set text color to light */
#     }}
#     /* Add white border to all boxes on the right side */
#     .block-container {{ /* This is a general container, might need refinement */
#         border: 1px solid white !important;
#         border-radius: 5px; /* Optional: add some rounding */
#         padding: 10px; /* Optional: add some padding inside the border */
#         margin-bottom: 10px; /* Optional: add some space between blocks */
#     }}
# 
# 
# </style>
# """
# 
# st.markdown(background_css, unsafe_allow_html=True)
# 
# 
# # Main header with gradient background
# st.markdown(
#     """
# <div class="main-header">
#     <h1>💼 Employee Salary Prediction & Classification App</h1>
#     <p style="font-size: 1.2rem; margin-bottom: 0;">
#         Predict whether an employee will earn > 50K or ≤50K using Machine Learning
#     </p>
# </div>
# """,
#     unsafe_allow_html=True,
# )
# 
# # Sidebar inputs (matching the original dataset features)
# st.sidebar.markdown("### 👤 Input Employee Details")
# st.sidebar.markdown("---")
# 
# # Personal Information Section
# st.sidebar.markdown("#### 🏠 Personal Information")
# age = st.sidebar.slider("Age", 17, 90, 39, help="Employee's age in years")
# gender = st.sidebar.selectbox(
#     "Gender", list(GENDER_MAPPING.keys()), help="Employee's gender"
# )
# race = st.sidebar.selectbox(
#     "Race", list(RACE_MAPPING.keys()), help="Employee's race/ethnicity"
# )
# # Use the keys from the dynamically generated or fallback mapping
# native_country = st.sidebar.selectbox(
#     "Native Country",
#     list(NATIVE_COUNTRY_MAPPING.keys()),
#     index=list(NATIVE_COUNTRY_MAPPING.keys()).index("United-States") if "United-States" in NATIVE_COUNTRY_MAPPING else 0,
#     help="Employee's country of origin",
# )
# 
# st.sidebar.markdown("---")
# 
# # Education Section
# st.sidebar.markdown("#### 🎓 Education")
# education = st.sidebar.selectbox(
#     "Education Level",
#     list(EDUCATION_NUM_MAPPING.keys()),
#     index=list(EDUCATION_NUM_MAPPING.keys()).index("Bachelors"),
#     help="Highest level of education completed",
# )
# 
# st.sidebar.markdown("---")
# 
# # Work Information Section
# st.sidebar.markdown("#### 💼 Work Information")
# workclass = st.sidebar.selectbox(
#     "Work Class",
#     list(WORKCLASS_MAPPING.keys()),
#     index=list(WORKCLASS_MAPPING.keys()).index("Private"),
#     help="Type of employer",
# )
# occupation = st.sidebar.selectbox(
#     "Occupation", list(OCCUPATION_MAPPING.keys()), help="Type of occupation/job role"
# )
# hours_per_week = st.sidebar.slider(
#     "Hours per week", 1, 99, 40, help="Average number of hours worked per week"
# )
# 
# st.sidebar.markdown("---")
# 
# # Family Information Section
# st.sidebar.markdown("#### 👨‍👩‍👧‍👦 Family Information")
# marital_status = st.sidebar.selectbox(
#     "Marital Status", list(MARITAL_STATUS_MAPPING.keys()), help="Current marital status"
# )
# relationship = st.sidebar.selectbox(
#     "Relationship",
#     list(RELATIONSHIP_MAPPING.keys()),
#     help="Relationship within household",
# )
# 
# capital_gain = st.sidebar.number_input(
#     "Capital Gain",
#     min_value=0,
#     max_value=99999,
#     value=0,
#     help="Capital gains from investments (annual)",
# )
# capital_loss = st.sidebar.number_input(
#     "Capital Loss",
#     min_value=0,
#     max_value=4356,
#     value=0,
#     help="Capital losses from investments (annual)",
# )
# fnlwgt = st.sidebar.number_input(
#     "Final Weight (Census)",
#     value=189778,
#     min_value=12285,
#     max_value=1484705,
#     help="Census final weight - represents similarity to other people",
# )
# 
# # Build input DataFrame (must match the exact preprocessing of training data)
# input_df = pd.DataFrame(
#     {
#         "age": [age],
#         "workclass": [WORKCLASS_MAPPING[workclass]],
#         "fnlwgt": [fnlwgt],
#         "educational-num": [EDUCATION_NUM_MAPPING[education]],
#         "marital-status": [MARITAL_STATUS_MAPPING[marital_status]],
#         "occupation": [OCCUPATION_MAPPING[occupation]],
#         "relationship": [RELATIONSHIP_MAPPING[relationship]],
#         "race": [RACE_MAPPING[race]],
#         "gender": [GENDER_MAPPING[gender]],
#         "capital-gain": [capital_gain],
#         "capital-loss": [capital_loss],
#         "hours-per-week": [hours_per_week],
#         "native-country": [NATIVE_COUNTRY_MAPPING[native_country]],
#     }
# )
# 
# # Create two columns for better layout
# col1, col2 = st.columns([2, 1])
# 
# with col1:
#     st.markdown("### 🔎 Input Data Preview")
#     st.markdown("The model will receive this preprocessed data:")
# 
#     # Display each field line by line in a more readable format
#     st.markdown("#### 📋 Processed Input Values:")
# 
#     # Create a clean display of all input values
#     input_data = [
#         ("👤 Age", age, "years"),
#         ("💼 Work Class", workclass, f"(encoded: {WORKCLASS_MAPPING[workclass]})"),
#         ("📊 Census Weight", f"{fnlwgt:,}", "final weight"),
#         (
#             "🎓 Education Level",
#             education,
#             f"(encoded: {EDUCATION_NUM_MAPPING[education]})",
#         ),
#         (
#             "💑 Marital Status",
#             marital_status,
#             f"(encoded: {MARITAL_STATUS_MAPPING[marital_status]})",
#         ),
#         ("🏢 Occupation", occupation, f"(encoded: {OCCUPATION_MAPPING[occupation]})"),
#         (
#             "👨‍👩‍👧‍👦 Relationship",
#             relationship,
#             f"(encoded: {RELATIONSHIP_MAPPING[relationship]})",
#         ),
#         ("🌍 Race", race, f"(encoded: {RACE_MAPPING[race]})"),
#         ("⚧ Gender", gender, f"(encoded: {GENDER_MAPPING[gender]})"),
#         ("💰 Capital Gain", f"${capital_gain:,}", "annual"),
#         ("📉 Capital Loss", f"${capital_loss:,}", "annual"),
#         ("⏰ Hours per Week", hours_per_week, "hours"),
#         (
#             "🏳 Native Country",
#             native_country,
#             f"(encoded: {NATIVE_COUNTRY_MAPPING[native_country]})",
#         ),
#     ]
# 
#     # Display in a clean format with alternating background
#     for i, (label, value, extra) in enumerate(input_data):
#         # Apply light text color for the details
#         st.markdown(f"<span style='color: #f8f8f2;'>{label}:** {value} {extra}</span>", unsafe_allow_html=True)
# 
# 
#     # Show the raw numerical array that goes to the model
#     with st.expander("🔢 Raw Model Input (Numerical Array)", expanded=False):
#         st.markdown("*This is the exact numerical data sent to the ML model:*")
#         model_input = input_df.values[0]
#         for i, (feature_name, value) in enumerate(zip(input_df.columns, model_input)):
#             st.write(f"{i+1}. *{feature_name}:* {value}")
# 
#         st.markdown("*As array:*")
#         st.code(str(model_input.tolist()))
# 
# with col2:
#     # Model information using native Streamlit components
#     st.markdown("#### 🤖 Model Overview")
# 
#     # Metrics in a clean layout
#     col2a, col2b = st.columns(2)
#     with col2a:
#         st.metric(label="🎯 Accuracy", value="85.71%")
#     with col2b:
#         st.metric(label="🔢 Features", value="13")
# 
#     st.markdown("---")
#     st.markdown("#### 📊 Technical Details")
# 
#     # Technical details in a clean format
#     st.markdown(
#         """
#     *Algorithm:* Gradient Boosting Classifier
#     *Training Samples:* 47,619
#     *Data Source:* UCI Adult Dataset
#     *Model Type:* Classification (Binary)
#     """
#     )
# 
#     # Additional info box
#     st.info("✨ This model achieved the highest accuracy among 5 tested algorithms!")
# 
# # Enhanced feature mapping section
# st.markdown("---")
# with st.expander("📋 View Feature Mappings & Model Details", expanded=False):
#     st.markdown("🔢 Categorical features are encoded as follows:")
# 
#     # Create tabs for better organization
#     tab1, tab2, tab3 = st.tabs(
#         ["👤 Personal & Work", "🎓 Education & Family", "🌍 Location & Demographics"]
#     )
# 
#     with tab1:
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("*Work Class:*")
#             st.json(WORKCLASS_MAPPING)
#             st.markdown("*Occupation:*")
#             st.json(OCCUPATION_MAPPING)
#         with col2:
#             st.markdown("*Marital Status:*")
#             st.json(MARITAL_STATUS_MAPPING)
#             st.markdown("*Relationship:*")
#             st.json(RELATIONSHIP_MAPPING)
# 
#     with tab2:
#         st.markdown("*Education Level (to educational-num):*")
#         st.json(EDUCATION_NUM_MAPPING)
# 
#     with tab3:
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("*Race:*")
#             st.json(RACE_MAPPING)
#             st.markdown("*Gender:*")
#             st.json(GENDER_MAPPING)
#         with col2:
#             st.markdown("*Native Country:*")
#             st.json(NATIVE_COUNTRY_MAPPING)
# 
# # Enhanced predict button with better styling
# st.markdown("---")
# col1, col2, col3 = st.columns([1, 2, 1])
# 
# with col2:
#     if st.button("🎯 Predict Salary Class", use_container_width=True):
#         with st.spinner("🤖 Analyzing employee data..."):
#             # Convert DataFrame to numpy array to match training format
#             prediction = model.predict(input_df.values)
# 
#             # Enhanced prediction display
#             if prediction[0] == ">50K":
#                 st.markdown(
#                     f"""
#                 <div class="prediction-success">
#                     💰 Prediction: {prediction[0]}
#                     <br><small>This employee is predicted to earn more than $50,000 annually</small>
#                 </div>
#                 """,
#                     unsafe_allow_html=True,
#                 )
#                 st.balloons()
#             else:
#                 st.markdown(
#                     f"""
#                 <div style="background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
#                            padding: 1rem; border-radius: 10px; color: white; text-align: center;
#                            font-size: 1.2rem; font-weight: bold;">
#                     📊 Prediction: {prediction[0]}
#                     <br><small>This employee is predicted to earn $50,000 or less annually</small>
#                 </div>
#                 """,
#                     unsafe_allow_html=True,
#                 )
# 
# # Enhanced batch prediction section
# st.markdown("---")
# st.markdown(
#     """
# <div style="background: linear-gradient(90deg, #ff7e5f 0%, #feb47b 100%); /* Bright gradient for the batch section */
#            padding: 1.5rem; border-radius: 10px; margin: 2rem 0; border: 2px solid white;"> /* White border for batch prediction header */
#     <h3 style="color: white; margin: 0;">📂 Batch Prediction</h3>
#     <p style="color: white; margin: 0.5rem 0 0 0;">
#         Upload a CSV file with the same 13 columns as shown above for bulk predictions
#     </p>
# </div>
# """,
#     unsafe_allow_html=True,
# )
# 
# # File uploader with better styling
# uploaded_file = st.file_uploader(
#     "Choose a CSV file",
#     type="csv",
#     help="Upload a CSV file with 13 columns matching the expected format",
# )
# 
# if uploaded_file is not None:
#     try:
#         with st.spinner("📊 Processing your file..."):
#             batch_data = pd.read_csv(uploaded_file)
# 
#         # Display file info
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.metric("📄 Rows", len(batch_data))
#         with col2:
#             st.metric("📊 Columns", len(batch_data.columns))
#         with col3:
#             st.metric("💾 File Size", f"{uploaded_file.size} bytes")
# 
#         st.markdown("📋 Uploaded data preview:")
#         st.dataframe(batch_data.head(), use_container_width=True)
# 
#         # Check if the uploaded data has the correct columns
#         expected_columns = [
#             "age",
#             "workclass",
#             "fnlwgt",
#             "educational-num",
#             "marital-status",
#             "occupation",
#             "relationship",
#             "race",
#             "gender",
#             "capital-gain",
#             "capital-loss",
#             "hours-per-week",
#             "native-country",
#         ]
# 
#         if list(batch_data.columns) == expected_columns:
#             with st.spinner("🤖 Making predictions..."):
#                 # Apply the same encoding to the batch data as the training data
#                 batch_data['workclass'] = batch_data['workclass'].map(WORKCLASS_MAPPING)
#                 batch_data['marital-status'] = batch_data['marital-status'].map(MARITAL_STATUS_MAPPING)
#                 batch_data['occupation'] = batch_data['occupation'].map(OCCUPATION_MAPPING)
#                 batch_data['relationship'] = batch_data['relationship'].map(RELATIONSHIP_MAPPING)
#                 batch_data['race'] = batch_data['race'].map(RACE_MAPPING)
#                 batch_data['gender'] = batch_data['gender'].map(GENDER_MAPPING)
#                 batch_data['native-country'] = batch_data['native-country'].map(NATIVE_COUNTRY_MAPPING)
# 
# 
#                 # Convert DataFrame to numpy array to match training format
#                 batch_preds = model.predict(batch_data.values)
#                 batch_data["PredictedClass"] = batch_preds
# 
#             # Show prediction summary
#             pred_counts = batch_data["PredictedClass"].value_counts()
#             col1, col2 = st.columns(2)
# 
#             with col1:
#                 st.markdown("📈 Prediction Summary:")
#                 for pred, count in pred_counts.items():
#                     percentage = (count / len(batch_data)) * 100
#                     st.write(f"• {pred}: {count} ({percentage:.1f}%)")
# 
#             with col2:
#                 st.markdown("✅ Predictions completed successfully!")
#                 st.dataframe(batch_data.head(10), use_container_width=True)
# 
#             # Download button with better styling
#             csv = batch_data.to_csv(index=False).encode("utf-8")
#             st.download_button(
#                 label="📥 Download Predictions CSV",
#                 data=csv,
#                 file_name="predicted_classes.csv",
#                 mime="text/csv",
#                 use_container_width=True,
#             )
#         else:
#             st.markdown(
#                 """
#             <div class="prediction-error">
#                 ❌ Column Mismatch Error
#                 <br><small>Your CSV must have these exact columns in order</small>
#             </div>
#             """,
#                 unsafe_allow_html=True,
#             )
# 
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.markdown("*Expected columns:*")
#                 for i, col in enumerate(expected_columns, 1):
#                     st.write(f"{i}. {col}")
#             with col2:
#                 st.markdown("*Your file has:*")
#                 for i, col in enumerate(batch_data.columns, 1):
#                     st.write(f"{i}. {col}")
# 
#     except Exception as e:
#         st.markdown(
#             f"""
#         <div class="prediction-error">
#             ❌ File Processing Error
#             <br><small>{str(e)}</small>
#         </div>
#         """,
#             unsafe_allow_html=True,
#         )
# 
# # About This Model section using native Streamlit components
# st.markdown("---")
# st.markdown("## 🚀 About This AI Model")
# st.markdown(
#     "An advanced machine learning solution for salary classification using demographic and professional features"
# )
# 
# # Create three columns for the metrics
# col1, col2, col3 = st.columns(3)
# 
# with col1:
#     st.markdown("### 🎯 High Accuracy")
#     st.metric(
#         label="Test Accuracy", value="85.71%", help="Validated performance on test data" # Update accuracy value
#     )
#     st.markdown("Best among 5 tested algorithms")
# 
# with col2:
#     st.markdown("### 📊 Rich Dataset")
#     st.metric(
#         label="Training Samples",
#         value="46,720", # Update training sample count
#         help="Training samples from UCI repository",
#     )
#     st.markdown("UCI Adult Census Dataset")
# 
# with col3:
#     st.markdown("### 🔢 Multi-Feature")
#     st.metric(
#         label="Input Features", value="13", help="Diverse demographic & work features"
#     )
#     st.markdown("Comprehensive feature set")
# 
# st.markdown("---")
# 
# # Technology stack
# st.markdown("### 🛠 Technology Stack")
# tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)
# 
# with tech_col1:
#     st.markdown("🐍 *Python*")
#     st.caption("Core language")
# 
# with tech_col2:
#     st.markdown("🧠 *Scikit-learn*")
#     st.caption("ML framework")
# 
# with tech_col3:
#     st.markdown("🚀 *Streamlit*")
#     st.caption("Web interface")
# 
# with tech_col4:
#     st.markdown("📊 *Pandas*")
#     st.caption("Data processing")
# 
# # Model comparison and data visualizations
# st.markdown("---")
# st.markdown("## 📊 Model and Data Visualizations")
# 
# with st.expander("📈 Model Performance Comparison", expanded=True): # Set expanded to True by default
#     st.markdown("*Comparison of different algorithms tested:*")
# 
#     perf_data = {
#         "Algorithm": [
#             "Gradient Boosting",
#             "Random Forest",
#             "Logistic Regression",
#             "SVM",
#             "KNN",
#         ],
#         "Accuracy": [0.8571, 0.8487, 0.7964, 0.7884, 0.7704], # Use numerical values for plotting
#         "Status": ["✅ Best", "🥈 Second", "🥉 Third", "4th", "5th"],
#     }
#     perf_df = pd.DataFrame(perf_data)
# 
#     # Plot the accuracy
#     fig, ax = plt.subplots(figsize=(10, 6))
#     sns.barplot(x="Algorithm", y="Accuracy", data=perf_df, ax=ax, palette="viridis")
#     ax.set_title("Model Accuracy Comparison")
#     ax.set_ylabel("Accuracy Score")
#     plt.xticks(rotation=45, ha='right')
#     plt.tight_layout()
#     st.pyplot(fig)
# 
#     st.dataframe(perf_df, use_container_width=True)
# 
# with st.expander("📊 Data Distribution - Age and Hours per Week", expanded=False):
#     st.markdown("*Distribution of Age and Hours per Week in the dataset:*")
# 
#     # Load the original data for plotting (assuming it's accessible)
#     try:
#         original_data = pd.read_csv("/content/adult 3.csv")
# 
#         col1, col2 = st.columns(2)
# 
#         with col1:
#             st.markdown("### Age Distribution")
#             fig, ax = plt.subplots(figsize=(6, 4))
#             sns.histplot(original_data['age'], bins=30, kde=True, ax=ax, color='skyblue')
#             ax.set_title("Distribution of Age")
#             ax.set_xlabel("Age")
#             ax.set_ylabel("Frequency")
#             plt.tight_layout()
#             st.pyplot(fig)
# 
#         with col2:
#             st.markdown("### Hours per Week Distribution")
#             fig, ax = plt.subplots(figsize=(6, 4))
#             sns.histplot(original_data['hours-per-week'], bins=30, kde=True, ax=ax, color='lightgreen')
#             ax.set_title("Distribution of Hours per Week")
#             ax.set_xlabel("Hours per Week")
#             ax.set_ylabel("Frequency")
#             plt.tight_layout()
#             st.pyplot(fig)
# 
#     except Exception as e:
#         st.warning(f"Could not load original data for plotting: {e}")
# 
# 
# with st.expander("👨‍👩‍👧‍👦 Distribution of Relationship Status", expanded=False):
#     st.markdown("*Distribution of Relationship Status in the dataset:*")
#     try:
#         original_data = pd.read_csv("/content/adult 3.csv")
#         fig, ax = plt.subplots(figsize=(10, 6))
#         sns.countplot(y='relationship', data=original_data, order = original_data['relationship'].value_counts().index, ax=ax, palette='pastel')
#         ax.set_title("Distribution of Relationship Status")
#         ax.set_xlabel("Count")
#         ax.set_ylabel("Relationship Status")
#         plt.tight_layout()
#         st.pyplot(fig)
#     except Exception as e:
#         st.warning(f"Could not load original data for plotting Relationship Status: {e}")
# 
# 
# # Footer
# st.markdown("---")
# st.markdown("Made by Jeet Shaw")
# st.caption("Employee salary Prediction Project")

!pip install streamlit pyngrok

!ngrok config add-authtoken 30EnMb6NPiJJt68rEzgMqc1ehmg_55psJd4mjRioeWhvUnTT7

import os
import threading

def run_streamit():
    os.system('streamlit run app.py --server.port 8501')

thread = threading.Thread(target=run_streamit)
thread.start()

from pyngrok import ngrok
import time

# Disconnect any existing ngrok tunnels
ngrok.kill()

time.sleep(5)  # Wait for Streamlit to start
public_url = ngrok.connect(8501)
print("🚀 Your app is live at:", public_url)

!streamlit run app.py





