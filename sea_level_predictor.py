import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", usecols=["Year", "CSIRO Adjusted Sea Level"])


    # Create scatter plot
    x = df["Year"].values
    y = df["CSIRO Adjusted Sea Level"].values
    plt.scatter(x = x, y = y)

    # Create first line of best fit
    firstResult = linregress(x, y)
    firstSlope = firstResult.slope
    firstIntercept = firstResult.intercept
    firstLineX = range(x[0], 2050)
    firstLineY = firstLineX * firstSlope + firstIntercept
    plt.plot(firstLineX, firstLineY, 'r')

    # Create second line of best fit
    df2 = df[(df['Year'] >= 2000)]
    x2 = df2["Year"].values
    y2 = df2["CSIRO Adjusted Sea Level"].values
    secondResult = linregress(x2, y2)
    secondSlope = secondResult.slope
    secondIntercept = secondResult.intercept
    secondLineX = range(x2[0], 2050)
    secondLineY = secondLineX * secondSlope + secondIntercept
    plt.plot(secondLineX, secondLineY, 'g')


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
