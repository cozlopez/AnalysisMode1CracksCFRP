import numpy as np
def filterr(threshold = 100, crack_open = 10, crack_threshold = 170, n_x = 30, n_y = 6 ): #n_x is the x neibourhood, n_y is the y neighborhoud
    #rgba(197,197,197,255)
    from PIL import Image
    import numpy as np
    

    image = Image.open("Crack11.png")
    image_array1 = np.array(image)

    if len(np.shape(image_array1)) == 2: #in case you don't have an alpha channel 
        alpha_ch = np.full_like(image_array1, 255)
        image_array1 = np.stack((image_array1, image_array1, image_array1, alpha_ch), axis=-1)
    
    
    new_image_array = np.where(image_array1 < threshold, 90, 255)

    shape = np.shape(new_image_array)
        
    func = False
    func2 = False
    func3 = False

    target_color = np.array([255, 255, 255, 255])
    target_color_2 = np.array([90,90,90,255])


    for col in range(shape[1]):
       
        for row in range(shape[0]):

            
            if np.array_equal(new_image_array[row][col], target_color) and func ==  False:
                new_image_array[row][col] = np.array([0, 0, 255, 255])
                func = True
                

            elif np.array_equal(new_image_array[row][col], target_color_2) and func2 == False and func == True:
                new_image_array[row][col] = np.array([0, 0, 255, 255])
                func2 = True
            
    
                crackpos1 = row 
                startcol = col 

            elif np.array_equal(new_image_array[row][col], target_color) and func ==  True and func2 == True and func3 == False:
                new_image_array[row][col] = np.array([0, 0, 255, 255])
                func3 = True

                crackpos2 = row
    
    new_image = Image.fromarray(new_image_array.astype('uint8'))
    new_image.show()


    new_image_array = np.where(image_array1 < crack_threshold, 90, 255)    
   
    new_image = Image.fromarray(new_image_array.astype('uint8'))
    new_image.show()

    
    
    for col in range(shape[1]):
       
        for row in range(crackpos1 - crack_open, crackpos2 + crack_open):
            
            if np.array_equal(new_image_array[row][col], target_color_2):
                new_image_array[row][col] = np.array([0,130,0,255])

    green = np.array([0,130,0,255])
    red = np.array([250,0,0,255])


    cont = True
    cont2 = True
    r = 0
    d = 0
    while cont == True: 
        if np.array_equal(new_image_array[crackpos1+d][startcol + r + 1], green):
            r += 1 
            new_image_array[crackpos1+d][startcol + r] = red

        elif np.array_equal(new_image_array[crackpos1+d - 1][startcol+r], green):
            d -=1
            new_image_array[crackpos1+d ][startcol+r] = red

        elif np.array_equal(new_image_array[crackpos1+d + 1][startcol+r], green):
            d += 1
            new_image_array[crackpos1+d ][startcol+r] = red
                
        else:
            cont = False


    #if in a certain rectangular box around the crack tip, there is a green block, consider those as a crack as well
    #you could also lower the threshold

    move_x = 0
    move_y = 0 
    move = True
    #for tryy in range(40):
    while move == True:
        move = False
        move_up = False
        move_down = False
        cols = []
        rows = []
        for col in range(0,n_x):
            
            for row in range(-n_y,n_y):
                if np.array_equal(new_image_array[crackpos1+d+row+move_y][startcol + r + 1 + col+move_x],green):
                    new_image_array[crackpos1+d+row+move_y][startcol + r + 1 + col+move_x] = red
                    move = True
                    cols.append(col)
                    rows.append(row)
                    
                    
        if move == True:    

            move_x += max(cols)
            move_y += max(rows)

         
            
            
                                  
        
    new_image = Image.fromarray(new_image_array.astype('uint8'))
    new_image.show()

    print(r + 2 + move_x) #which is the pixel crack length 
    #return r + 2 + move_x


filterr()
