import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def hourly_patterns():
    """"
    Makes a bar plot of crime frequency by hour of day
    
    Output:
    - Saves the plot to data/analyzed/hourly_patterns_plot.png
    """

    path = "data/analyzed/hourly_patterns.csv"
    df = pd.read_csv(path)

    #create a bar plot using seaborn 

    plt.figure(figsize=(10, 6))
    sns.barplot(x='hour', y='crime_count', data=df, palette="viridis")
    plt.title("Crime Frequency by Hour of Day")
    plt.xlabel("Hour (0-23)")
    plt.ylabel("Crime Count")

    #save the plot
    output_path = "data/analyzed/hourly_patterns_plot.png"
    plt.savefig(output_path)
    print(f"Saved plot to {output_path}")