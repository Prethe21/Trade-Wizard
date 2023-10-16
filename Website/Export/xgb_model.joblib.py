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

# Make predictions on the test set
predictions = xgb_regressor.predict(X_test)

# Calculate and print the evaluation metrics
mse = mean_squared_error(y_test, predictions)
r_squared = r2_score(y_test, predictions)

print("Mean Squared Error:", mse)
print("R-squared:", r_squared)

# Save the model
joblib.dump(xgb_regressor, 'xgb_model.joblib')
