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


## Pipeline Evaluation
The primary goal of this project is to create a reliable and reproducible data cleaning pipeline. Therefore, the evaluation of this project is not based on traditional machine learning metrics like accuracy or F1-score, but on engineering-focused metrics:

1.  **Correctness:** The `pytest` suite in the `/tests` folder contains unit tests that verify each cleaning function behaves exactly as expected. A successful run of `pytest` proves the logical correctness of the pipeline.
2.  **Reproducibility:** The final "clean room" test (Mission 7.1) proves that the entire project is reproducible by another user on a different machine, confirming the integrity of the documentation and the `requirements.txt` file.


## Challenges & Learnings
Throughout this project, several technical challenges were encountered and overcome:
* **Pathing and Reproducibility:** A key challenge was managing file paths (`FileNotFoundError`) and Python's import system (`ModuleNotFoundError` during testing). This was solved by establishing a robust project structure, using relative paths correctly (`data/...` vs `../data/...`), and modifying `sys.path` in the test setup. These solutions were validated by the final reproducibility test.
* **Test Maintenance:** As the main `clean_data` function grew more complex (e.g., adding date conversion), the unit tests initially failed due to missing columns in the sample data (`KeyError`). This highlighted the importance of keeping test data synchronized with the function's requirements.
* **Version Control Synchronization:** A `git push` was rejected due to divergence between the local and remote repositories. This common issue was resolved using `git pull` to merge the remote changes before successfully pushing the combined history, reinforcing a crucial real-world Git workflow.


## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/sidhardhsmlai/reproducible-data-pipeline.git
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
