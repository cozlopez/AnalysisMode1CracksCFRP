import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Load the CSV data into a pandas DataFrame


# Plot the two columns

# Calculate the linear regression line

for i in range(3):
    df = pd.read_csv('Sample'+str(i+1)+'.csv')
    slope, intercept, r, p, se = sp.stats.linregress(np.array(df['C1/3']), np.array(df['a_mm']))
    linear_regression = slope * df['C1/3'] + intercept
    print(slope,intercept)

    plt.figure(figsize=(10,6))

    # Plot the two columns
    plt.plot(df['C1/3'], df['a_mm'], label='Data')

    # Plot the linear regression line
    plt.plot(df['C1/3'], linear_regression, color='red', label='Linear Regression')

    # Add labels and title to the plot
    plt.xlabel('$ C^{\\frac{1}{3}} $')
    plt.ylabel('$a_{mm}$ ')
    plt.title('Test 1 + Linear Regression Line')

    # Add a legend to the plot
    plt.legend()

    # Save the plot as an image file in the current folder
    plt.savefig('linear_regression_plot'+str(i+1)+'.png')



