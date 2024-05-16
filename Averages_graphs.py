import numpy as np
import matplotlib.pyplot as plt

def plot_multiple_linear_relations(params_list, x_range=(100, 100000),y_range = (0,1.2), num_points=100):
    # Generate x values within the specified range
    fig,ax = plt.subplots()
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    i = 0
    # Plot each linear relationship with a different color
    for m, c, color in params_list:
        i=i + 1
        # Calculate y values using the linear equation y = mx + c
        y_values = 10**(m *np.log10( x_values )+ c)
        # Plot the linear relationship with the specified color
        if i<6:
            ax.plot(x_values, y_values, label='User '+ str(i), color=color)
        if i==6:
            ax.plot(x_values, y_values, label='Hop method', color=color, linestyle='dashed')
        if i==7:
            ax.plot(x_values, y_values, label='Manual average', color=color, linestyle='dashed')
    
    ax.set_xlabel('log(# Cycles)')
    ax.set_ylabel('log($a-a_0$)')
    ax.set_xscale('log', base=10)
    ax.set_yscale('log', base=10)
    
    
    
    ax.grid(True)
    ax.legend()
    plt.show()


# Example usage
# List of tuples containing (m, c, color) values for each linear relationship
params_list = [(0.13961015, 0.244581091, 'blue'), (0.127710895, 0.361831674, 'red'), (0.150545781, 0.222005088, 'green'), (0.129464013, 0.35345854, 'purple'), (0.139692833, 0.277140293, 'orange'),(0.142851183,0.238651294,"black"),(0.137404734,0.291803337,"cyan")]
plot_multiple_linear_relations(params_list)
