from Image_legnth_manual import display_image

for i in range (2):
    image_width = 5852  # Width of the image in pixels
    scale_factor = 0.5  # Scale factor for the distance calculation
    distance = display_image("Test"+str(i+1)+".png", scale_factor, image_width)
    image_width = 5852  # Width of the image in pixels
    scale_factor = 0.5  # Scale factor for the distance calculation
