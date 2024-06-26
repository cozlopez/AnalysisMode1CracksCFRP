import pygame as pg 
import sys
import os
import csv
import tkinter as tk
from resizing import resize
from tkinter import simpledialog


root = tk.Tk()
#root.withdraw()  # Hide the main window

# Ask for user input
name = simpledialog.askstring("Input", "Please enter your name:", parent=root)
num_samples = simpledialog.askinteger("Input", "Please enter the number of samples:", parent=root)

root.destroy()


def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")






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

# Function to handle the folder selection
def select_folder(evt):
    selected_folder.set(listbox.get(listbox.curselection()))
    print("Selected Folder:", selected_folder.get())
    root.after(1000, root.destroy)  # Close the window after 1000 milliseconds

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

# After the window is closed, the selected folder can be retrieved from the StringVar
print("Selected Folder (after window closed):", selected_folder.get())

# Add your existing code here
image_dir = selected_folder.get()  # Relative path to the image















#from Image_legnth_manual import display_image


distances_list = []
pg.init()
# basic program settings
infoObject = pg.display.Info()
scale = 0.95
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







def display_image(image_path,scalefactor,iteration): # TODO: Place real scale factor.
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
        


lst = os.listdir(os.path.join(os.getcwd(),"Images", image_dir))
base_path = os.path.join(os.getcwd(),"Images", image_dir)
print(os.path.join(os.getcwd(),"Images", image_dir))
number_files = len(lst)



print(selected_folder.get())
if selected_folder.get() == "01" or selected_folder.get() == "04":
    scalefactor = 0.03054367746
elif selected_folder.get() == "02":
    scalefactor = 0.03381355932
elif selected_folder.get() == "03":
    scalefactor = 0.03846153846



file_name = "measurements_images_"+str(image_dir)+'_'+str(name)+'_'+ 'iteration_' +str(num_samples)+".csv"






# Create a csv file to store the measurements
with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Image Number", "Distance in mm", "Distance in pixels"])


delete_files_in_directory(os.getcwd() + "/Zoomed_images")

for i in range(number_files-1):
    image_path = str(base_path) + "/" + str(int(image_dir)) + " (" + str(i + 1) + ").jpg"
    image_path_resize= os.getcwd() + "/" + "Zoomed_images"
    if not os.path.exists(image_path):
        print("File not found:", image_path)

    else:
        
        #print(image_path_resize)
        try:
            resize(5,image_path_resize,image_path,image_path_resize)  
        except:
            resize(2,image_path_resize,image_path,image_path_resize)
    
        


for i in range(number_files - 1):
    image_path_2= os.getcwd() + "/" + "Zoomed_images"+"/" + str(int(image_dir)) + " (" + str(i + 1) + ").jpg"

    if not os.path.exists(image_path_2):
        print("File not found:", image_path_2)
        continue
    distance = display_image(image_path_2, scalefactor,i)
    print(scalefactor)
    print("Distance:", distance)
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["1({}).jpg".format(str(i + 1)), distance * scalefactor, distance])

        
        
        
    



