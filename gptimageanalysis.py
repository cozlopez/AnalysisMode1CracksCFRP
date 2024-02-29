import cv2
import numpy as np
from matplotlib import pyplot as plt

def calculate_crack_length(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Apply edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # Apply morphological operations to close gaps in the crack edges
    kernel = np.ones((3,3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)
    
    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Assuming the largest contour is the crack, we find the longest one
    longest_contour = max(contours, key=cv2.contourArea)
    
    # Draw contours on the original image for visualization (optional)
    contour_image = np.copy(image)
    cv2.drawContours(contour_image, [longest_contour], -1, (255, 0, 0), 2)

    # Calculate the length of the contour
    # Each contour point consists of an array of points; we use the Euclidean distance between each consecutive point
    crack_length_pixels = np.sum([cv2.norm(longest_contour[i][0], longest_contour[i+1][0], cv2.NORM_L2)
                                  for i in range(len(longest_contour) - 1)])

    # Convert the pixel measurement to millimeters using the provided scale (1 mm per vertical line)
    # As the image may not be perfectly aligned, we assume that the scale provided is accurate for the image's resolution
    crack_length_mm = crack_length_pixels / image.shape[1] * 2048  # 2048 pixels in the image represent 2048 mm

    return crack_length_mm

# Path to the image
image_path = '/Test1.png'

# Calculate the crack length
crack_length = calculate_crack_length(image_path)
print(f"The length of the crack is approximately {crack_length:.2f} mm.")