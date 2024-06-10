from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import IsolationForest, GradientBoostingClassifier

app = Flask(__name__)

# Load pre-trained models
iso_forest = IsolationForest()
gbm = GradientBoostingClassifier()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    iso_pred = iso_forest.predict(df)
    gbm_pred = gbm.predict(df)
    return jsonify({'IsolationForest': iso_pred.tolist(), 'GBM': gbm_pred.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
