import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Load the CSV data into a pandas DataFrame


# Plot the two columns

# Calculate the linear regression line

for i in range(4):
    df = pd.read_csv('Sample'+str(i+1)+'.csv')
    slope, intercept, r, p, se = sp.stats.linregress(np.array(df['a_mm']), np.array(df['C1/3']))
    linear_regression = slope * df['a_mm'] + intercept
    print(slope,intercept)
    print(linear_regression)
    plt.figure(figsize=(10,6))

    # Plot the two columns
    plt.scatter(df['a_mm'], df['C1/3'], label='Data')
    plt.xlim(np.min(df['a_mm'])-1, np.max(df['a_mm'])+1)
    plt.ylim(np.min(df['C1/3'])-1e-5, np.max(df['C1/3'])+1e-5)

    # Plot the linear regression line
    plt.plot(df['a_mm'], np.array(linear_regression), color='red', label='Linear Regression')

    # Add labels and title to the plot
    plt.ylabel('$ C^{\\frac{1}{3}} $')
    plt.xlabel('$a_{mm}$ ')
    plt.title('Test'+str(i+1) + '+ Linear Regression Line')

    # Add a legend to the plot
    plt.legend()

    # Save the plot as an image file in the current folder
    plt.savefig('linear_regression_plot'+str(i+1)+'.png')



