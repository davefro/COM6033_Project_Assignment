from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from joblib import load
import json
import logging

# init logging for debugging and monitoring
logging.basicConfig(level=logging.DEBUG)

# create a Flask app
app = Flask(__name__)

# load the model and scaler
model = load('random_forest_model.joblib')
sale_price_scaler = load('sale_price_scaler.joblib')

# load feature configuration files
with open('selected_features.json', 'r') as f:
    selected_features = json.load(f)

with open('ui_features_names.json', 'r') as f:
    ui_features_names = json.load(f)

with open('ordinal_mappings.json', 'r') as f:
    ordinal_mappings = json.load(f)

# ensure features are consistent
assert set(selected_features) == set(ui_features_names.keys()), "Features mismatch!"

@app.route('/')
def home():
    return render_template('index.html', ui_features_names=ui_features_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        #parse input data from the form
        data = request.form.to_dict()
        logging.debug(f"Raw input data: {data}")

        #  handle binary features (checkbox inputs)
        binary_features = ['Foundation_PConc', 'BsmtFin Type 1_GLQ']
        for feature in binary_features:
            data[feature] = int(data.get(feature, 0))  
        
        # Apply ordinal mappings for categorical features
        for col, mapping in ordinal_mappings.items():
            if col in data:
                data[col] = mapping.get(data[col])  

        # prepare feature vector
        features = [float(data[feature]) for feature in ui_features_names.keys()]
        features_df = pd.DataFrame([features], columns=ui_features_names.keys())
        logging.debug(f"Feature DataFrame for prediction: {features_df}")

        # make predictions
        prediction_scaled = model.predict(features_df)
        prediction_original = sale_price_scaler.inverse_transform(
            prediction_scaled.reshape(-1, 1)
        ).flatten()[0]
        logging.debug(f"Predicted price: {prediction_original}")

        # Redirect to the result page with the prediction
        return redirect(url_for('result', price=round(prediction_original, 2)))

    except Exception as e:
        # log errors if something is wrong
        print(f"Error during prediction: {e}")
        return render_template('index.html', error="An error occurred. Please try again."), 500

@app.route('/result')
def result():
    # Retrieve the price from the query parameter
    price = request.args.get('price')
    if not price:
        return "Prediction not found.", 400
    return render_template('result.html', price=price)


if __name__ == '__main__':
    app.run(debug=True)
