import numpy as np
import matplotlib.pyplot as plt

def plot_multiple_linear_relations(params_list, x_range=(2, 5),y_range = (0,1.2), num_points=100):
    # Generate x values within the specified range
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    i = 0
    # Plot each linear relationship with a different color
    for m, c, color in params_list:
        i=i + 1
        # Calculate y values using the linear equation y = mx + c
        y_values = m * x_values + c
        # Plot the linear relationship with the specified color
        plt.plot(x_values, y_values, label='Sample '+ str(i), color=color)
    
    plt.xlabel('log(Number of Cycles)')
    plt.ylabel('log($a-a_0$)')
    plt.title('Multiple Linear Relationships')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
# List of tuples containing (m, c, color) values for each linear relationship
params_list = [(0.13961015, 0.244581091, 'blue'), (0.127710895, 0.361831674, 'red'), (0.150545781, 0.222005088, 'green'), (0.129464013, 0.35345854, 'purple'), (0.139692833, 0.277140293, 'orange')]
plot_multiple_linear_relations(params_list)
