from resize import resize
from crack2 import filterr
from scaling import scale
import numpy as np
import os



a_0smm = [50.35,51.50,50.79,50.87] 
a_0s = [106,207,120,69]
mults = []
lengths = []
scales = []
folder = 3
th = 192
#th for folder 3 = 192
#th for folder 4 = 190
#for other th = 180
#n_x was 30 before now I changed to 33 for folder 3



for num in range(200):
    filee = str(folder)+' ('+str(num)+').jpg'
    
    
    if filee in os.listdir('/Users/fedorselivanov/Documents/Image recognition/Images/0'+str(folder)):
        if filee != ".DS_Store": #and count < 10:
            file = filee
            #print(file) 
            try:
                resized = resize('Images/0'+str(folder)+'/'+file, 5)
                
            except:
                resized = resize('Images/0'+str(folder)+'/'+file, 3)

            diff = a_0s[folder -1]
            #mult = 2/66.3
            #mult = 2/56 #for folder 3
            mult = 1
            #print(file)
            lengths.append(round((filterr(resized,th, False) - diff)*mult,3)) #if true displays the cracks

            
            with open(str(folder)+'Outputs.csv', 'a') as fil:
                    
                    fil.write(str(   round((filterr(resized,th, False)- diff)*mult,3)     ) + " , " + str(file[2:]) + "\n")

            
            
            
            #print(file)
            """
            try:
                scales.append(scale(resized))

            except:
                scales.append("error")
            """
            
        #count += 1



print(lengths)
#print(scales)
   

"""
for x in range(30):
    try:
        
        lengths.append(filterr(resized, th))

        th += 1

    except:

        lengths.append("error")

mini = min.lengths


for x in range(30):
    if lengths[x] 


print(lengths)
"""
    
        



        

    
    
