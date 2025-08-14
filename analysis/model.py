import pandas as pd
import os
from sklearn.cluster import KMeans

def run_model(processed_path):
    """
    Runs  clstering  model on the processed LAPD crime data
    saves to data/outputs/.
    """
    print("Running KMeans clustering model...")
    df = pd.read_csv(processed_path)

    outputs_dir = os.path.join("data", "outputs")
    os.makedirs(outputs_dir, exist_ok=True)

    coords = df[['lat', 'lon']].dropna()
    kmeans = KMeans(n_clusters=5, random_state=42)
    coords['cluster'] = kmeans.fit_predict(coords)

    cluster_counts = coords['cluster'].value_counts().reset_index(name='crime_count')
    cluster_counts.rename(columns={'index': 'cluster'}, inplace=True)
    cluster_counts.to_csv(os.path.join(outputs_dir, "area_hotspots.csv"), index=False)

    print(f"Model results saved to {outputs_dir}")
    return outputs_dir