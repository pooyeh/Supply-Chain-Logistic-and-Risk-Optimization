import pandas as pd

def load_and_preprocess_data(input_csv):
    # Load data
    data = pd.read_csv(input_csv)

    # Preprocess data (example: filling missing values)
    data.fillna(method='ffill', inplace=True)

    return data

if __name__ == "__main__":
    input_csv = 'data/rfid_sensor_data.csv'
    processed_data = load_and_preprocess_data(input_csv)
    processed_data.to_csv('data/processed_data.csv', index=False)
