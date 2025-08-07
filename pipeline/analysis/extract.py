import os
import pandas as pd


def extract_data(file_path = "Crime_Data_from_2020_to_Present.csv"):

    """
    Extracts raw crime data from a CSV file and saves it to a specified directory.

    Parameters:
    - file_path: Path to the raw crime data CSV file (default is "Crime_Data_from_2020_to_Present.csv")
    Output:
    - Saves the raw data to data/raw/crime_data_raw.csv
    Returns:
    - The path to the saved raw data file.
    """
    
                 
    print ("Extracting")
    #simulate download 
    input_data = "Crime_Data_from_2020_to_Present.csv"

    #Load CSV file
    df = pd.read_csv(input_data)

    #save raw data copy
    raw_data = os.path.join("data", "raw")
    os.makedirs(raw_data, exist_ok=True)
    raw_path = os.path.join(raw_data, "crime_data_raw.csv")
    df.to_csv(raw_path, index=False)

    print(f"Raw data saved to {raw_path}")
    return raw_path