import pandas as pd
import psycopg2

def store_data_to_redshift(input_csv, redshift_table, redshift_credentials):
    # Load data
    data = pd.read_csv(input_csv)

    # Connect to Redshift
    conn = psycopg2.connect(
        dbname=redshift_credentials['dbname'],
        user=redshift_credentials['user'],
        password=redshift_credentials['password'],
        host=redshift_credentials['host'],
        port=redshift_credentials['port']
    )
    cur = conn.cursor()

    # Create table if not exists
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {redshift_table} (
        timestamp TIMESTAMP,
        sensor_id VARCHAR(50),
        temperature FLOAT,
        humidity FLOAT,
        label VARCHAR(50)
    );
    """
    cur.execute(create_table_query)
    conn.commit()

    # Insert data into Redshift
    for _, row in data.iterrows():
        insert_query = f"""
        INSERT INTO {redshift_table} (timestamp, sensor_id, temperature, humidity, label)
        VALUES ('{row['timestamp']}', '{row['sensor_id']}', {row['temperature']}, {row['humidity']}, '{row['label']}');
        """
        cur.execute(insert_query)
    conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
    input_csv = 'data/labeled_data.csv'
    redshift_table = 'your_redshift_table'
    redshift_credentials = {
        'dbname': 'your_dbname',
        'user': 'your_user',
        'password': 'your_password',
        'host': 'your_host',
        'port': 'your_port'
    }
    store_data_to_redshift(input_csv, redshift_table, redshift_credentials)
