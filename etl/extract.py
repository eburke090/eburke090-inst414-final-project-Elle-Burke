import os
import pandas as pd

def extract_data(url="https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"):
    """
    Downloads raw LAPD crime data and saves to data/raw/.
    """
    print("Extracting raw data from LAPD source...")
    extracted_dir = os.path.join("data", "extracted")
    os.makedirs(extracted_dir, exist_ok=True)
    extracted_path = os.path.join(extracted_dir, "crime_data_raw.csv")

    # Download and save
    df = pd.read_csv(url)
    df.to_csv(extracted_path, index=False)

    print(f"Raw data saved to {extracted_path}")
    return extracted_path
