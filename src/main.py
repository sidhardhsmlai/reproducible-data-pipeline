import pandas as pd
def load_data(filepath):
    """
    Loads a CSV file from the given filepath into a pandas DataFrame,
    specifying the correct encoding.
    """
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    return df

if __name__== "__main__":
    file_path = 'data/online_retail.csv'
    retail_df= load_data(file_path)
    print("Data loaded successfully. Here are the first 5 rows:")
    print(retail_df.head())
