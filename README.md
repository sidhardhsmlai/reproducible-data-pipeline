# Reproducible Data Pipeline

## Project Overview
This project is an automated data cleaning pipeline built in Python using Pandas. It takes the raw, messy Online Retail dataset and transforms it into a clean, analysis-ready format by handling missing values, removing invalid transactions, and standardizing data types. This project serves as a demonstration of foundational data engineering and software development best practices.

## Dataset
The data used is the [Online Retail Dataset](https://www.kaggle.com/datasets/vijayuv/onlineretail) from the UCI Machine Learning Repository. It contains transactional data for a UK-based online retailer.

## Tools Used
* Python
* Pandas
* Pytest

## Cleaning Pipeline Steps
The `clean_data` function in `src/main.py` performs the following sequential steps:
1.  Drops all rows where the `CustomerID` is missing.
2.  Removes all cancelled orders (transactions where `InvoiceNo` starts with 'C').
3.  Converts the `InvoiceDate` column to the proper datetime format.
4.  Ensures both `Quantity` and `UnitPrice` are positive by filtering out non-positive values.
5.  Converts the `CustomerID` column to a clean integer data type.

## How to Run
1. Clone the repository:
   ```bash
   git clone <https://github.com/sidhardhsmlai/reproducible-data-pipeline.git>
   ```
2. Navigate into the project directory:
   ```bash
   cd reproducible-data-pipeline
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the cleaning pipeline:
   ```bash
   python src/main.py
   ```
   The cleaned data will be saved to `data/clean_online_retail.csv`.

## How to Run Tests
To verify the functionality of the cleaning logic, run the test suite:
```bash
pytest