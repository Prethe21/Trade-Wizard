#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load and preprocess the data
data = pd.read_excel('train.xlsx')

# Convert categorical variables to one-hot encoding
data = pd.get_dummies(data, columns=['Reporting Economy', 'Product/Sector'], drop_first=True)

X = data.drop('Value', axis=1)
y = data['Value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the XGBoost Regressor model
xgb_regressor = XGBRegressor(random_state=42)
xgb_regressor.fit(X_train, y_train)

# Save the model
joblib.dump(xgb_regressor, 'xgb_model.joblib')

# Load the model
loaded_model = joblib.load('xgb_model.joblib')

# Prepare the input for prediction
# You need to provide all 283 features that the model was trained on
# If you don't have these features, you won't be able to use this model for prediction
input_data = [[0, 0, 2021] + [0]*280]  # Assuming the first three features are 0

# Make predictions
new_predictions = loaded_model.predict(input_data)
print("Predicted Value:", new_predictions[0])


# In[ ]:





# In[ ]:




