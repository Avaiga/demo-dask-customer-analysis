# demo-dask-customer-analysis

##demo description
This article focuses on the seamless integration of Dask (for handling out-of-core data) with Taipy, a Python library used for pipeline orchestration and scenario management.

This readme covers a data workflow with 4 tasks:

- Data Preprocessing and Customer Scoring

- Read and process a large dataset using Dask.
Feature Engineering and Segmentation

- Score customers based on purchase behavior.
Segment Analysis: Segment customers into different categories based on scores and other factors.

- Summary Statistics for High-Value Customers
Analyze each customer segment to derive insights.


## file description
```
algos/
├─ algo.py  #  Our existing code with 4 tasks
data/
├─ SMALL_amazon_customers_data.csv  #  A sample dataset
app.ipynb  # Jupyter Notebook for running our sample data application
config.py  # Taipy configuration which models our data workflow
config.toml  # (Optional) Taipy configuration in TOML made using Taipy Studio
```
