import cv2
import numpy as np

# Load the image
image = cv2.imread('Test1.png', cv2.IMREAD_GRAYSCALE)

# Threshold the image to binary using Otsu's binarization
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Perform morphological operations to remove small black regions
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Find contours in the binary image
contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the maximum area (this should be the region of interest)
max_contour = max(contours, key=cv2.contourArea)

# Create a mask of the region of interest
mask = np.zeros_like(image)
cv2.drawContours(mask, [max_contour], -1, (255), thickness=cv2.FILLED)

# Create an inverse of the mask
inverse_mask = cv2.bitwise_not(mask)

# Apply the inverse mask to the original image to get the ignored regions
ignored_regions = cv2.bitwise_and(image, inverse_mask)

# Display the ignored regions
cv2.imshow('Ignored Regions', ignored_regions)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bitwise-and the mask with the original image
roi = cv2.bitwise_and(image, mask)

# Display the region of interest
cv2.imshow('Region of Interest', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find contours in the ROI
contours, _ = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the maximum area (this should be the black crack)
max_contour = max(contours, key=cv2.contourArea)

# Find the furthest point in the contour
furthest_point = max(max_contour, key=lambda x: x[0][0] + x[0][1])

# Convert the grayscale image to BGR
image_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Draw a red cross at the furthest point
cv2.drawMarker(image_bgr, tuple(furthest_point[0]), (0, 0, 255), cv2.MARKER_CROSS, 20, 2)

# Draw a line from the left start of the image along the x-axis to the furthest point
cv2.line(image_bgr, (0, furthest_point[0][1]), tuple(furthest_point[0]), (0, 0, 255), 2)

# Calculate the middle point of the x-axis
middle_point = (0, image_bgr.shape[0] // 2)

# Draw a line from the middle of the x-axis at the leftmost side of the image to the crack tip
cv2.line(image_bgr, middle_point, tuple(furthest_point[0]), (0, 255, 0), 2)

# Display the final image
cv2.imshow('Final Image', image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Calculate the length of the line
length = np.sqrt((furthest_point[0][0] - 0) ** 2 + (furthest_point[0][1] - furthest_point[0][1]) ** 2)

# Draw a thicker line to represent the length
cv2.line(image_bgr, (0, furthest_point[0][1]), (int(length), furthest_point[0][1]), (0, 255, 0), 5)

# Display the final image with the length line
cv2.imshow('Final Image with Length Line', image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the final image to a file
cv2.imwrite('output_image.png', image_bgr)

# Print the length
print("Length of the line:", length)

# Modify the color scale of the grayscale image
color_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)

# Display the modified color image
cv2.imshow('Modified Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()