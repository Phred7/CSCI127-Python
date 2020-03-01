import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------
# CSCI 127, Lab 13
# November 27, 2018
# Your Name
# -------------------------------------------------

def main():

    data_frame = pd.read_csv("billionaires.csv")

    poorest_billionaire = data_frame["worth in billions"].min()
    print("Poorest", poorest_billionaire)


    richest_billionaire = data_frame["worth in billions"].max()
    print("Richest", richest_billionaire)

    average_billionaire = data_frame["worth in billions"].mean()
    print("Average", average_billionaire)

    # Figure 1 is a scatter plot
    data_frame.plot.scatter(x="age", y="worth in billions", color="xkcd:turquoise", marker=".")
    plt.title("Billionaire Age Scatter Plot")

    # Figure 2 is a pie chart
    color = ["xkcd:gold", "xkcd:royal blue"]
    plt.figure()
    data_frame["sector"].value_counts()[:10].plot.pie(colors=color)
    plt.title("Billionaire Industry Pie Chart")

    # Figure 3 is a bar chart
    plt.figure()
    plt.title("Billionaire Location Bar Chart")
    plt.xlabel("Region")
    plt.ylabel("Total Net Worth")
    data_object = data_frame.groupby("region")
    print(data_object.describe())
    condensed_data_frame = data_object.sum()
    print(condensed_data_frame)

    condensed_data_frame = condensed_data_frame[1:]
    condensed_data_frame["worth in billions"].plot.bar()
    plt.xticks(np.arange(7), ("E Asia", "Europe", "C Amer", "N Afr", "N Amer", "S Asia", "S Afr"))
    
    plt.show()

# -------------------------------------------------

main()
