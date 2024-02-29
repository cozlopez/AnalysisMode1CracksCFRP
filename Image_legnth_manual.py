import math
from PIL import Image, ImageTk
import tkinter as tk
import pygame as pg
from Test import *

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

'''
def display_image(image_path, scale_factor, image_width):
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
'''
def display_image(image_path, scale_factor, image_width):
    # Display image
    while True:
        screen.blit(image_path,(0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT: # Checks if the user has pressed the close (X) button or pressed alt + F4
                sys.exit()



