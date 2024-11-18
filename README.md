# Mini Project 11: Data Pipeline with Databricks
#### The purpose of this project is to perform a ETL workflow on a csv file that has been loaded into databricks, and utilize a personal compute to run the pipeline

#### Requirements:

- [X] Create a data pipeline using Databricks
- [X] Include at least one data source and one data sink
- [X] Pipeline functionality 
- [X] Data source and sink configuration
- [X] CI/CD pipeline
- [X] README.md
- [X] Databricks notebook or script
- [X] Document or video demonstrating the pipeline


---
### Folder Navigation
##### Here is a quick overview of how the folders are structured for this project:
---
- Project Folder
    - .devcontainer
        - devcontainer.json
        - Dockerfile
    - .github
        - workflows
            - main.yml
    - data
        - Table 1 csv file
    - SQL_files
        - extract.py
        - transform.py (includes query)
        - query_log.md (markdown that logs all queries made)
    - Makefile
    - README.md
    - requirements.txt
    - test_main.py
---
### Workflow Summary and Explanation
##### This project contains the following dependencies:
- pylint == 2.15.3
- black == 22.3.0
- pytest == 7.1.3
- ruff == 0.0.284
- fire == 0.7.0
- requests == 2.32.3
- pandas == 2.2.2
- python-dotenv == 1.0.1
- databricks-sql-connector == 3.4.0
---
### What is the Purpose of this Project?
##### This project demonstrates the functionality of an ETL (Extract, Transform, Load) pipeline using Databricks. The pipeline is designed to automate the extraction of data from a source, apply transformations, and load the data into a sink. The pipeline extracts data from a CSV file located at a publicly accessible GitHub repo. This file contains contains information about remote workers and their mental health status. The ETL pipeline in this project follows the core principles of data engineering:

- Extract: Pull data from a defined data source (A GitHub Repo in this case)
- Transform: Perform necessary transformations on the extracted data
- Load: Load the transformed data into a destination for further use or analysis


##### First, the data was extracted from was established, and the data was transformed/cleaned and loaded as two tables (remote_health1) into the databricks. 

##### Finally, after the tables are successfully loaded into the database, any type of query can be performed to explore the data. 

___
### What is the Goal of the Query?
##### In this project, the query I ran can be seen in the query_log.md file, or in the screenshots below. First, I selected the first 5 rows from the data. Once it was determined that the data was accessible via a query, I selected the total count of employees, grouped the data by industry, and then ordered the data in descending order. Finally, I found the average number of hours worked per week, based on the industry. 

##### Query:

##### Result:

##### Table of Results


##### This table displays the results in a more visual way, grouped by industry. We are able to directly compare the number of employees in each industry, and the average hours worked per week.



