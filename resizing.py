

#from PIL import Image
#from PIL import ImageColor
#import numpy as np


def resize(file, min_crack_length):
    from PIL import Image
    from PIL import ImageColor
    import numpy as np

    #Provide image file path and extract the variable "crack_centered_image"


    image = Image.open(file)
    rgb_image = image.convert('RGB')

    width, height = image.size
    color_matrix = np.zeros((height, width))
    color_value = ImageColor.getrgb("red")

    for y in range(height):
        r, g, b = rgb_image.getpixel((0, y))
        color = [r, g, b]

        if r > 100 and g > 100 and b > 100:
            y_sample_start = y
            break
        
    y_start_crack = 0
    y_end_crack = 0
    start_crack_triguered = False
    end_crack_triguered = False
    for i in range(y_sample_start, height):
        r, g, b = rgb_image.getpixel((0, i))
        color = [r, g, b]
        
        if r < 50 and g < 50 and b < 50 and not start_crack_triguered:
            y_start_crack = i
            start_crack_triguered = True
            
        if r > 100 and g > 100 and b > 100 and start_crack_triguered:
            y_end_crack = i
            end_crack_triguered = True
            
        if y_start_crack != 0 and y_end_crack != 0:
            break

    need_to_flip = True
    if abs(y_start_crack - y_end_crack) > min_crack_length and y_start_crack != 0 and y_end_crack != 0:
        need_to_flip = False

    if need_to_flip:
        rgb_image_transformed = rgb_image.transpose(Image.FLIP_LEFT_RIGHT)
        rgb_image_transformed = rgb_image_transformed.convert("RGB")
        
        y_start_crack_2 = 0
        y_end_crack_2 = 0
        y_sample_start_2 = 0
        y_sample_end_2 = 0
        start_crack_triguered_2 = False
        end_crack_triguered_2 = False
        start_sample_triguered_2 = False
        end_sample_triguered_2 = False
        for j in range(0, height):
            r, g, b = rgb_image_transformed.getpixel((0, j))
            color = [r, g, b]
        
            if r > 100 and g > 100 and b > 100 and not start_sample_triguered_2:
                y_sample_start_2 = j
                #rgb_image_transformed.putpixel((0, y_sample_start_2), (255, 0, 0))
                start_sample_triguered_2 = True

            if r < 50 and g < 50 and b < 50 and start_sample_triguered_2 and not start_crack_triguered_2:
                y_start_crack_2 = j
                start_crack_triguered_2 = True
                #rgb_image_transformed.putpixel((0, y_start_crack_2), (255, 0, 0))
            
            if r > 100 and g > 100 and b > 100 and start_sample_triguered_2 and start_crack_triguered_2 and not end_crack_triguered_2:
                y_end_crack_2 = j
                end_crack_triguered_2 = True
                #rgb_image_transformed.putpixel((0, y_end_crack_2), (255, 0, 0))
            
            if r < 50 and g < 50 and b < 50 and start_sample_triguered_2 and start_crack_triguered_2 and end_crack_triguered_2 and not end_sample_triguered_2:
                y_sample_end_2 = j
                end_sample_triguered_2 = True
                #rgb_image_transformed.putpixel((0, y_sample_end_2), (255, 0, 0))
                break

        #rgb_image_transformed.show()
        #print(y_sample_start_2, y_sample_end_2, end_sample_triguered_2)
        crack_centered_image = rgb_image_transformed.crop((0, y_sample_start_2 - 60, 700, y_sample_end_2 + 60))
        #crack_centered_image.show()
        return crack_centered_image 
        

    else:
        y_start_crack_2 = 0
        y_end_crack_2 = 0
        y_sample_start_2 = 0
        y_sample_end_2 = 0
        start_crack_triguered_2 = False
        end_crack_triguered_2 = False
        start_sample_triguered_2 = False
        end_sample_triguered_2 = False
        for j in range(y_sample_start, height):
            r, g, b = rgb_image.getpixel((0, j))
            color = [r, g, b]
        
            if r > 100 and g > 100 and b > 100 and not start_sample_triguered_2:
                y_sample_start_2 = j
                #rgb_image.putpixel((0, y_sample_start_2), (255, 0, 0))
                start_sample_triguered_2 = True

            if r < 50 and g < 50 and b < 50 and start_sample_triguered_2 and not start_crack_triguered_2:
                y_start_crack_2 = j
                start_crack_triguered_2 = True
                #rgb_image.putpixel((0, y_start_crack_2), (255, 0, 0))
            
            if r > 100 and g > 100 and b > 100 and start_sample_triguered_2 and start_crack_triguered_2 and not end_crack_triguered_2:
                y_end_crack_2 = j
                end_crack_triguered_2 = True
                #rgb_image.putpixel((0, y_end_crack_2), (255, 0, 0))
            
            if r < 50 and g < 50 and b < 50 and start_sample_triguered_2 and start_crack_triguered_2 and end_crack_triguered_2 and not end_sample_triguered_2:
                y_sample_end_2 = j
                end_sample_triguered_2 = True
                #rgb_image.putpixel((0, y_sample_end_2), (255, 0, 0))
                break

        #rgb_image.show()
        
        crack_centered_image = rgb_image.crop((0, y_sample_start_2 - 60, 700, y_sample_end_2 + 60))
        #crack_centered_image.show()
        return crack_centered_image

#resize("Crack5.png")