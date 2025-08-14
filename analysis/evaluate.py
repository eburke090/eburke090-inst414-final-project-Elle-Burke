import pandas as pd
import os

def evaluate_data(processed_path):
    """
    Evaluates the processed LAPD crime data for basic statistics and saves the report to data/reports/.
    """
    print("Evaluating processed data...")
    df = pd.read_csv(processed_path)

    outputs_dir = os.path.join("data", "outputs")
    os.makedirs(outputs_dir, exist_ok=True)

    #monthly trends
    df['Incident_Date'] = pd.to_datetime(df['Incident Date'], errors='coerce')
    monthly = df.groupby(df['Incident_Date'].dt.to_period('M')).size().reset_index(name='crime_count')
    monthly.to_csv(os.path.join(outputs_dir, "monthly_trends.csv"), index=False)

    #hourly trends
    df['hour'] = pd.to_datetime(df['time'], format='%H: %M: %S', errors='coerce').dt.hour
    hourly = df.groupby('hour').size().reset_index(name='crime_count')
    hourly.to_csv(os.path.join(outputs_dir, "hourly_trends.csv"), index=False)

    print(f"Evaluation reports saved to {outputs_dir}")
    return outputs_dir