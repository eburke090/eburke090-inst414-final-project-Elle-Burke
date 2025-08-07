from pipeline.analysis.extract import extract_data
from pipeline.analysis.transform_load import transform_data
from pipeline.visualize.monthly_trends import plot_monthly_trends
from pipeline.visualize.hourly_patterns import plot_hourly_patterns
from pipeline.visualize.hotspots import plot_hotspots


def run_pipeline():
    print(">>>Starting pipeline<<<")

    # A. Extract
    raw_path = extract_data()

    # B. Transform and Load
    processed_path = transform_data(raw_path)

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