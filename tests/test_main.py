import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))#still not usre what it does ,but solved the trouble accessing src 


from src.main import clean_data

def test_removes_cancelled_orders():
    # 1. Setup: Create sample data
    data = {
    'InvoiceNo': ['536365', 'C536379'], 
    'CustomerID': [17850, 14527],
    'InvoiceDate': ['12/1/2010 8:26', '12/1/2010 9:41'], 
    'Quantity': [1, -1],
    'UnitPrice': [1.0, 1.0]                             
    }

    df = pd.DataFrame(data)
    # 2. Action: Run the function we are testing
    cleaned_df = clean_data(df)

    assert cleaned_df.shape[0] ==1
    assert cleaned_df['InvoiceNo'].iloc[0]=='536365'


def test_removes_rows_with_missing_customer_id():
    # 1. Setup: One valid row, one with a missing CustomerID
    
    data = {
    'InvoiceNo': ['536365', '536366'],
    'CustomerID': [17850, None],
    'InvoiceDate': ['12/1/2010 8:26', '12/1/2010 8:28'],
    'Quantity': [1, 1],
    'UnitPrice': [1.0, 1.0]
    }
    df = pd.DataFrame(data)
    # 2. Action
    cleaned_df = clean_data(df)

    assert cleaned_df.shape[0]==1
    assert cleaned_df['CustomerID'].iloc[0]==17850
    
