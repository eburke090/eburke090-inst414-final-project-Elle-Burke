import pandas as pd
import os
import matplotlib.pyplot as plt

def monthly_trends():

    """
    Generates a line plot of monthly crime trends.
    Output:
    - Saves the plot to data/analyzed/monthly_trends_plot.png
    """

    # Load the data
    path = "data/analyzed/monthly_trends.csv"
    df = pd.read_csv(path)
    #convert period string to datetime format for plotting 
    df['month'] = pd.to_datetime(df['month'].astype(str))
    
    #create line plot using matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(df['month'], df['crime_count'], marker='o')
    plt.title("Monthly Crime Trends")
    plt.xlabel("Month")
    plt.ylabel("Crime Count")
    plt.grid(True)

    #save plot
    output_path = "data/analyzed/monthly_trends_plot.png"
    plt.savefig(output_path)
    print(f"Saved plot to {output_path}")