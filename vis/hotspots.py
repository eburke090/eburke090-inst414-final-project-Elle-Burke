import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_hotspots(top_n=10):
    """
    Genertes a bar plot of the top N crime hotspots by area.

    Parameters:
    - top_n: Number of top hotspots to display (default is 10)

    Output:
    - Saves the plot to data/analyzed/hotspots_plot.png
    """

    #loades data
    path = "data/analyzed/hotspots_by_area.csv"
    df = pd.read_csv(path).head(top_n)

    #creat horizonal bar plot using seaborn 
    plt.figure(figsize=(10, 6))
    sns.barplot(y='area_name', x='crime_count', data=df, palette="rocket")
    plt.title(f"Top {top_n} Crime Hotspots by Area")
    plt.xlabel("Crime Count")
    plt.ylabel("Area")

    #save the plot
    output_path = "data/analyzed/hotspots_plot.png"
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Saved plot to {output_path}")