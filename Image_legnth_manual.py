import math
from PIL import Image, ImageTk
import tkinter as tk

# Define an empty list to store the distances
distances = []

def calculate_distance(image_width, scale_factor, event):
    # Get the x-coordinate of the clicked point
    chosen_point = event.x

    # Calculate the distance to the start of the image
    distance = chosen_point * scale_factor

    # Print the result
    print("Distance to the start of the image in the x-axis:", distance)

    # Append the distance to the distances list
    distances.append(distance)


def display_image(image_path):
    # Create a Tkinter window
    root = tk.Tk()

    # Load the image
    image = Image.open(image_path)

    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)

    # Create a label with the image
    label = tk.Label(root, image=photo)
    label.image = photo  # Keep a reference to the image to prevent it from being garbage collected

    # Bind the click event to the label
    label.bind("<Button-1>", lambda event: calculate_distance(image.width, scale_factor, event))

    # Display the label
    label.pack()

    # Run the Tkinter event loop
    root.mainloop()

# Example usage
image_width = 1000  # Width of the image in pixels
scale_factor = 0.5  # Scale factor for the distance calculation

image_path = "Falcon 9.png" # Replace with the actual path to your image
display_image(image_path)

# Print the distances list
print("Distances:", distances)