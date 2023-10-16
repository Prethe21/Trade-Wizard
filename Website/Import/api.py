from flask import Flask, request, jsonify
import joblib

app = Flask(__name)

# Load the XGBoost model
loaded_model = joblib.load('xgb_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid data format'}), 400

        # Ensure data has the same format as the model input
        if 'Reporting Economy' not in data or 'Product/Sector' not in data or 'Year' not in data:
            return jsonify({'error': 'Missing required data'}), 400

        # Prepare the input for prediction
        input_data = [
            data['Reporting Economy'],
            data['Product/Sector'],
            data['Year']
        ]

        # Make predictions
        prediction = loaded_model.predict([input_data])[0]

        # Return the predicted value
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
