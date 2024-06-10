import boto3

def catalog_data_in_aws_glue(bucket_name, file_key):
    client = boto3.client('glue')
    response = client.create_table(
        DatabaseName='your-database-name',
        TableInput={
            'Name': 'rfid_sensor_data',
            'StorageDescriptor': {
                'Columns': [
                    {'Name': 'timestamp', 'Type': 'timestamp'},
                    {'Name': 'sensor_id', 'Type': 'string'},
                    {'Name': 'temperature', 'Type': 'float'},
                    {'Name': 'humidity', 'Type': 'float'},
                ],
                'Location': f's3://{bucket_name}/{file_key}',
                'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                'Compressed': False,
                'NumberOfBuckets': -1,
                'SerdeInfo': {
                    'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                    'Parameters': {'field.delim': ','}
                }
            },
            'TableType': 'EXTERNAL_TABLE'
        }
    )
    return response

if __name__ == "__main__":
    bucket_name = 'your-s3-bucket'
    file_key = 'data/processed_data.csv'
    catalog_data_in_aws_glue(bucket_name, file_key)
