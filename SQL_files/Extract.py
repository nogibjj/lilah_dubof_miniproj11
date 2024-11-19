# Databricks notebook source
import requests
from pyspark.sql import SparkSession
import os

# COMMAND ----------

file_path = "/FileStore/tables/table_1_remote_work_mental_health_data.csv"
# Extracting data from GitHub
def extract(file_path, url="https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_1_remote_work_mental_health_data.csv"):

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Request data from URL
    response = requests.get(url)
 
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f"File downloaded successfully: {file_path}")
        return file_path
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        return None
