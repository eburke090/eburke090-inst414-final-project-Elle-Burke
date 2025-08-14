import os 
import pandas as pd


def transform_data(raw_path):

    """
    Transforms raw crime data by cleaning, processing, and saving it to a specified directory.
    Steps:
    - Remove rows with missing values in critical columns
    - Convert date columns to datetime format
    - Remove duplicate entries
    - Create a unique ID for each record
    - Rename columns for consistency
    
    
    Parameters:
    - raw_path: Path to the raw crime data CSV file.
    Output:
    - Saves the processed data to data/processed/crime_clean.csv
    Returns:
    - The path to the saved processed data file.
    """

    print("Transforming data")

    #CLEANING 
    #remove rows with missing values
    df = df.dropna(subset=['DATE', 'TIME', 'Crime Desc'])

    #convert date column to datetime
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')

    #delete duplicates
    df = df.drop_duplicates()

    #create a unique ID if not already present
    df.reset_index(drop=True, inplace=True)
    df['ID'] = df.index + 1

    #rename columns for consistency
    df.rename(columns={'Crime Desc': 'Crime_Description', 'DATE': 'Incident_Date'}, inplace=True)

    print("Top 5 crime types:")
    print(df['Crime_Description'].value_counts().head())

    print("\nDate range:")
    print(df['Incident_Date'].min(), "to", df['Incident_Date'].max())

    #save processed file
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    processed_path = os.path.join(processed_dir, "crime_clean.csv")
    df.to_csv(processed_path, index=False)

    print(f"Processed data saved to {processed_path}")
    return processed_path