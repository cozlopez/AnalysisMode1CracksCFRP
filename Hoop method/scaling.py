def scale(name):

    from PIL import Image
    import numpy as np

    """
    image = Image.open(name)
    image_array = np.array(image)
    """
    
    image_array = np.array(name) 

    image_array = image_array[:,:,0]

    if len(np.shape(image_array)) == 2: #in case you don't have an alpha channel 
        alpha_ch = np.full_like(image_array, 255)
        image_array = np.stack((image_array, image_array, image_array, alpha_ch), axis=-1)

    new_image_array = np.where(image_array < 100, 90, 255)


    shape = np.shape(new_image_array)

    white = np.array([255, 255, 255, 255]) #the material
    grey = np.array([90,90,90,255]) #the rest

    func = False 

    for col in range(20):

        for row in range(shape[0]-1, -1, -1):

            if np.array_equal(new_image_array[row][col], white) and func ==  False:
                new_image_array[row+1][col] = np.array([0,255,0,255])
                func = True
                startcol = col
                startrow = row
                

    startrow -= 10

    func2 = False

    

    for col in range(shape[1]):
        
        if np.array_equal(new_image_array[startrow][col], grey) and func2 == False:
            new_image_array[startrow][col + 3] = np.array([0,255,0,255])
            func2 = True
            mark = col + 3
            #print(mark)
    """
    new_image = Image.fromarray(new_image_array.astype('uint8'))
    new_image.show()
    """
                     
    return mark 
    
    


#scale("Crack4.png")
