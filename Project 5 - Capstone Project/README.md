# Data Engineering Capstone Project
## Project Summary

To building an ETL-Pipeline with Spark I loaded a ny-crime dataset from the OpenData Platform of NY and processed
 it together with weather and airbnb data from Kaggle.
 The data gets transformed into an relational data model and passed to an postgreSQL database.
 
 

# Files in the repository

* **[CapstoneProject.ipynb](CapstoneProject.ipynb)**: Main JupyterNotebook containing Database creation and Spark ETL Pipeline.
* **[LoadData.ipynb](LoadData.ipynb)**: Downloading the projectfiles from private S3 and saving them as parquet inside the project.
* **[sql_queries.py](sql_queries.py)**: Containing all SQL Queries needed to create the database.
* **[aws.cfg](aws.cfg)**: File for aws credentials.


If the notebooks doesn't get loaded you can use the nbviewer from jupyter: https://nbviewer.jupyter.org/

# The database schema design.

<img src="./images/ERD.png?raw=true" width="600" />

# Dataset used

* **NY Crime**: https://www1.nyc.gov/site/nypd/stats/crime-statistics/historical.page
* **NY Airbnb**: https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
* **NY Weather**: https://www.kaggle.com/mathijs/weather-data-in-new-york-city-2016
