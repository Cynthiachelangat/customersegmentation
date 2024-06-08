from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained KMeans model
with open('kmeans_elbow_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# Load the StandardScaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

@app.route('/')
def home():
    return "KMeans Clustering Model Deployment using Flask"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get the JSON data from the request
    df = pd.DataFrame(data)
    
    # Ensure all features are present
    expected_features = ['BALANCE', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 
                         'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 
                         'PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 
                         'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 
                         'PRC_FULL_PAYMENT', 'TENURE']
    
    if not all(feature in df.columns for feature in expected_features):
        return jsonify({"error": "Missing required features in the input data"}), 400

    # Standardize the input features
    X_scaled = scaler.transform(df[expected_features])

    # Predict the cluster for the input data
    clusters = kmeans_model.predict(X_scaled)

    # Add the cluster labels to the original data
    df['Cluster'] = clusters

    # Return the result as JSON
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
