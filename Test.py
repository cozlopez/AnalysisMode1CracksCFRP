#from Image_legnth_manual import display_image
import pygame as pg 
import sys
import os
import csv
import tkinter as tk

distances_list = []
pg.init()
# basic program settings
infoObject = pg.display.Info()
scale = 1
scrnx = infoObject.current_w*scale
scrny = infoObject.current_h*scale
resolution = (scrnx, scrny)
windowTitle = "Distance Calculator"
maxFrameRate = 120

# initialise Pygame

screen = pg.display.set_mode(resolution)
pg.display.set_caption(windowTitle)
clock = pg.time.Clock()
pg.font.init()
font1 = pg.font.SysFont('Arial', 20)








# Function to handle the folder selection
def select_folder(evt):
    selected_folder.set(listbox.get(listbox.curselection()))
    print("Selected Folder:", selected_folder.get())
    root.after(1000, root.destroy)  # Close the window after 1000 milliseconds




















def display_image(image_path,scalefactor =2): # TODO: Place real scale factor.
    diff = float()
    diffOG = float()
    image = pg.image.load(image_path)
    imgH = image.get_height()
    imgW = image.get_width()
    imageScale = imgH/imgW
    image = pg.transform.scale(image, (scrnx, scrnx*imageScale))
    firstPress = False
    firstPressX = float()
    secondPress = False
    secondPressX = float()
    thirdPress = False
    fourthPress = False
    confirmation = font1.render("Press again to confirm, press escape to choose again", True, (255,255,255))
    # Display image
    while True:
        screen.fill((0,0,0))
        screen.blit(image,(0,0))
        (mouseX,mouseY) = pg.mouse.get_pos()
        if not secondPress:
            pg.draw.line(screen, (255,0,0), (mouseX,0), (mouseX,scrny))
        if firstPress == True:
            pg.draw.line(screen, (0,255,0), (firstPressX,0), (firstPressX,scrny))
        if secondPress == True:
            pg.draw.line(screen, (0,255,0), (secondPressX,0), (secondPressX,scrny))
            if thirdPress == False:
                screen.blit(confirmation, (200,500))
        if thirdPress == True:
            dataText = font1.render("The distance on your screen is " + str(abs(diff)) + " pixels", True, (255,255,255))
            dataText2 = font1.render("The distance in the original image is " + str(abs(diffOG)) + " pixels", True, (255,255,255))
            dataText3 = font1.render("The distance in real life is "+ str(diffOG*scalefactor) + "mm",True, (255,255,255))
            dataText4 = font1.render("The distance in mm has been saved to the list. Click again to go to the next image or exit.", True, (255,255,255))
            screen.blit(dataText, (200,600))
            screen.blit(dataText2, (200,650))
            screen.blit(dataText3, (200,700))
            screen.blit(dataText4,(200,750))
            
        pg.display.update()
        clock.tick(maxFrameRate)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if firstPress == False:
                        firstPress = True
                        firstPressX = mouseX
                    elif firstPress == True and secondPress == False:
                        secondPress = True
                        secondPressX = mouseX
                    elif firstPress == True and secondPress == True and thirdPress == False:
                        thirdPress = True
                        diff = abs(secondPressX - firstPressX)
                        diffOG = diff*(imgW/scrnx)
                    elif firstPress == True and secondPress == True and thirdPress == True:
                        fourthPress = True
                        return diffOG
            if event.type == pg.QUIT: # Checks if the user has pressed the close (X) button or pressed alt + F4
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    firstPress = False
                    secondPress = False
        pg.event.pump()
        










# Create the root window
root = tk.Tk()

# Set the title of the window
root.title("Folder Selection")

# Set the size of the window
root.geometry("400x200")

# Get the list of subfolders in the directory
base_dir = os.path.join(os.getcwd(), "Images")
subfolders = [f.name for f in os.scandir(base_dir) if f.is_dir()]

# Create a StringVar to store the selected folder
selected_folder = tk.StringVar()





# Create a Label to display a message
label = tk.Label(root, text="Please select a folder:")
label.pack(pady=10)

# Create a Listbox to display the subfolders
listbox = tk.Listbox(root)
listbox.pack(pady=20)

# Add the subfolders to the Listbox
for folder in subfolders:
    listbox.insert(tk.END, folder)

# Bind the select_folder function to the Listbox selection event
listbox.bind('<<ListboxSelect>>', select_folder)

# Run the main event loop
root.mainloop()



image_dir = selected_folder.get()  # Relative path to the image directory
lst = os.listdir(os.path.join(os.getcwd(), image_dir))

print(os.path.join(os.getcwd(), image_dir))
number_files = len(lst)










# Create a csv file to store the measurements
with open('measurements.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Image Number", "Distance in mm"])


for i in range (number_files - 1):
    distance = display_image(str(base_path)+"/Images/1 ("+str(i+1)+").jpg")
    with open('measurements.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["1({}).jpg".format(str(i+1)), distance])


        
        
    



