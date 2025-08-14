from etl.extract import extract_data
from etl.transform_load import transform_data
from analysis.evaluate import evaluate_data
from analysis.model import run_model
from vis.monthly_trends import plot_monthly_trends
from vis.hourly_patterns import plot_hourly_patterns
from vis.hotspots import plot_hotspots


def run_pipeline():
    print(">>>Starting pipeline<<<")

    # A. Extract
    extracted_path = extract_data()

    # B. Transform and Load
    processed_path = transform_data(extracted_path)

    # C. Analysis - Evaluate
    evaluate_data(processed_path)

    # D. Analysis - Model
    run_model(processed_path)

    print(">>>Pipeline completed successfully!<<<")
    print(f"Processed data available at: {processed_path}")

def run_visualizations():
    print(">>>Starting visualizations<<<")
    plot_monthly_trends()
    plot_hourly_patterns()
    plot_hotspots()

if __name__ == "__main__":
    run_pipeline()
    run_visualizations()