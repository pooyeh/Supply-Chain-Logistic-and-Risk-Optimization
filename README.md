# Supply-Chain-Logistic-and-Risk-Optimization
![image](https://github.com/pooyeh/Supply-Chain-Logistic-and-Risk-Optimization/assets/13261352/23b6fb32-ff4e-4d66-a4d0-009313926bee)

# Pharmaceutical Supply Chain Automation

## Description

This project automates the supply chain process for a pharmaceutical company using RFID sensor data and AWS services. The workflow includes data collection, preprocessing, cataloging, model training, and deployment using Flask API containerized with Docker.

## Steps

1. **Data Collection and Preprocessing**: Load and preprocess data from CSV files.
2. **Data Cataloging Using AWS Glue**: Store raw data in AWS S3 and catalog using AWS Glue.
3. **Model Training**: Train models using Isolation Forest and Gradient Boosting Machine.
4. **Store Labeled Data in AWS Redshift**: Store labeled data in AWS Redshift.
5. **Containerize Flask API**: Containerize the Flask API for deployment on AWS.

## Files

- `data_preprocessing.py`: Script for data preprocessing.
- `aws_glue_catalog.py`: Script for cataloging data in AWS Glue.
- `train_model.py`: Script for training machine learning models.
- `store_to_redshift.py`: Script for storing labeled data in AWS Redshift.
- `Dockerfile`: Dockerfile for containerizing the Flask API.
- `app.py`: Flask API for model prediction.
- `requirements.txt`: Python dependencies for the Flask API.

## How to Run

### Build Docker Image

```bash
docker build -t flask-api .
