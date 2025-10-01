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
    return df


if __name__== "__main__":
    file_path = 'data/online_retail.csv'
     # 1. Load the data
    retail_df= load_data(file_path)
    print(f"Rows before cleaning:{retail_df.shape[0]}")
     # 2. Clean the data
    retail_df_clean = clean_data(retail_df)
    print(f"Rows after cleaning:{retail_df_clean.shape[0]}")\
    # 3. Print the head of the *cleaned* dataframe
    print("cleaned data.here are first 5 rows: ")
    print(retail_df_clean.head())