import pandas as pd
def load_data(filepath):
    """
    Loads a CSV file from the given filepath into a pandas DataFrame,
    specifying the correct encoding.
    """
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    return df




def clean_data(df):
    """
    Cleans the raw retaildata by handling missing values and removing return.
    """
    # --- Fix Problem 1: Handle Missing CustomerIDs ---
    df.dropna(subset=['CustomerID'], inplace=True)
    # --- Fix Problem 2: Remove Cancelled Orders (Returns) ---
    df=df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    # --- Fix Data types: Convert InvoiceDate to Datetime ---
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    # --- Final Numeric Sanity Check ---#
    df=df[df['Quantity']>0]
    df=df[df['UnitPrice']>0]
    # --- Final Type Conversion for CustomerID ---
    df['CustomerID']= df['CustomerID'].astype(int)

    return df


if __name__== "__main__":
    file_path = 'data/online_retail.csv'

     # 1. Load the data
    retail_df= load_data(file_path)
    print(f"Rows before cleaning:{retail_df.shape[0]}")

     # 2. Clean the data
    retail_df_clean = clean_data(retail_df)
    print(f"Rows after cleaning:{retail_df_clean.shape[0]}")
    
    # 3. Print the head of the *cleaned* dataframe
    print("cleaned data.here are first 5 rows: ")
    print("\nVerifying data types after cleaning:")
    print(retail_df_clean.info())
    print(retail_df_clean.head())
    print("retail_df_clean.describe RESULTS")
    print(retail_df_clean.describe())
    
    # 4. Save the cleaned data to a new file
    output_path= 'data/clean_online_retail.csv'
    retail_df_clean.to_csv(output_path, index=False)
    print(f" Cleaned data successfully saved to: {output_path}")
