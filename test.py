import cv2
import numpy as np

# Load the image and the chroma key
image = cv2.imread('Test1.png', cv2.IMREAD_GRAYSCALE)
chroma_key = cv2.imread('ChromaKey.png')

# Threshold the image to binary using Otsu's binarization
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find white lines in the binary image
y_coords, x_coords = np.where(binary == 255)

# Find the y-coordinate of the lowest white line
lowest_y_coord = np.max(y_coords)

# Create a mask of the same size as the chroma key, filled with ones (white)
mask = np.ones(chroma_key.shape[:2], dtype=np.uint8) * 255

# Black out everything below the lowest white line in the mask
mask[lowest_y_coord:, :] = 0

# Apply the mask to the chroma key using bitwise-and
updated_chroma_key = cv2.bitwise_and(chroma_key, chroma_key, mask=mask)

# Display the updated chroma key
cv2.imshow('Updated Chroma Key', updated_chroma_key)
cv2.waitKey(0)
cv2.destroyAllWindows()