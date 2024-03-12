from resize import resize
from crack2 import filterr
import numpy as np

lengths = []

file = "Crack13.png"
th = 170

try:
    resized = resize(file, 5)

except:
    resized = resize(file, 3)
    


for x in range(30):
    try:
        
        lengths.append(filterr(resized, th))

        th += 1

    except:

        lengths.append("error")
"""
mini = min.lengths


for x in range(30):
    if lengths[x] 
"""

print(lengths)

    
        



        

    
    
