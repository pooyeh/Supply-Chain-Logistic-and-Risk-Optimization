import pandas as pd
from sklearn.ensemble import IsolationForest, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_models(input_csv):
    # Load data
    data = pd.read_csv(input_csv)

    # Features and target
    X = data[['sensor_id', 'temperature', 'humidity']]
    y = data['label']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Isolation Forest
    iso_forest = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    iso_forest.fit(X_train)
    y_pred_iso = iso_forest.predict(X_test)
    
    # Gradient Boosting Machine
    gbm = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
    gbm.fit(X_train, y_train)
    y_pred_gbm = gbm.predict(X_test)

    print("Isolation Forest Classification Report:")
    print(classification_report(y_test, y_pred_iso))

    print("Gradient Boosting Machine Classification Report:")
    print(classification_report(y_test, y_pred_gbm))

if __name__ == "__main__":
    input_csv = 'data/processed_data.csv'
    train_models(input_csv)
