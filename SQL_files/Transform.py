# Databricks notebook source
import pandas as pd

LOG_FILE = "query_log.md"


def log_query(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

def load(dataset="/FileStore/tables/table_1_remote_work_mental_health_data.csv"):
    """ Transforms and Loads data into Databricks delta lake table"""
    spark = SparkSession.builder.appName("load_data").getOrCreate()
    remote_health_df = spark.read.csv(dataset, header=True, inferSchema=True)
    remote_health_df = remote_health_df.withColumn("Employee_ID", monotonically_increasing_id())
    remote_health_df.write.format("delta") \
        .option("mergeSchema", "true") \
        .mode("overwrite") \
        .saveAsTable("RemoteHealthTable")
    print("Successfully transformed and loaded data to Databricks")
    return "Success"

if __name__=="__main__":
    load()

# COMMAND ----------

def describe(table_name):
    """Performs summary stats on the table"""
    # Spark SQL query to describe the table structure and statistics
    query_stats = f"DESCRIBE EXTENDED {table_name}"
    
    try:
        stats_result_df = spark.sql(query_stats)
        stats_pandas_df = stats_result_df.toPandas()
        stats_result_str = stats_pandas_df.to_markdown(index=False)
        log_query(query, result=stats_result_str)
        return stats_pandas_df
    
    except Exception as e:
        error_message = f"Error while describing table {table_name}: {str(e)}"
        log_query(query, result=error_message)
        raise



# COMMAND ----------

def query(query: str, delta_table_name: str, table_name: str = None, overwrite=True):
    try:
        # Check if delta_table_name is provided
        if not delta_table_name:
            raise ValueError(f"Delta table name must be provided, provided: {delta_table_name}")
        
        # If no table name is provided, extract from delta_table_name
        table_name = table_name or delta_table_name.split(".")[-1]
        table_name = f"`{table_name}`"  
        log_query(query, result="Query received, executing next...")
        print(f"Executing SQL query on table {delta_table_name}")
        
        # Execute the query
        result_df = spark.sql(query)
        pandas_df = result_df.toPandas()
        
        # Convert the df to markdown
        result_str = pandas_df.to_markdown(index=False)  
        log_query(query, result=result_str)
        return result_df
    
    except Exception as e:
        # Catch and log any errors during the query execution
        error_message = f"Error occurred: {e}"
        log_query(query, result=error_message)
        print(error_message)
        return None 


# COMMAND ----------


outputdf = query("""SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM RemoteHealthTable
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;""",
        "RemoteHealthTable")

stats_output = query("""SELECT Industry, 
    AVG(Hours_Worked_Per_Week) AS avg_hours_worked
    FROM RemoteHealthTable
    GROUP BY Industry
    ORDER BY avg_hours_worked DESC;""", "RemoteHealthTable")
