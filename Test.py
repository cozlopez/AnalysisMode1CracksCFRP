#from Image_legnth_manual import display_image
import pygame as pg 
import sys
import os


distances = []

# basic program settings
scrnx = 1800
scrny = 1000
resolution = (scrnx, scrny)
windowTitle = "Distance Calculator"
maxFrameRate = 120

# initialise Pygame
pg.init()
screen = pg.display.set_mode(resolution)
pg.display.set_caption(windowTitle)
clock = pg.time.Clock()
pg.font.init()
font1 = pg.font.SysFont('Arial', 20)


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
            dataText3 = font1.render("The distance in the original image has been saved to the list. Click again to go to the next image or exit.", True, (255,255,255))
            screen.blit(dataText, (200,600))
            screen.blit(dataText2, (200,650))
            screen.blit(dataText3, (200,700))
            
        pg.display.update()
        clock.tick(maxFrameRate)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if firstPress == False:
                    firstPress = True
                    firstPressX = mouseX
                elif firstPress == True and secondPress == False:
                    secondPress = True
                    secondPressX = mouseX
                elif firstPress == True and secondPress == True and thirdPress == False:
                    thirdPress = True
                    diff = secondPressX - firstPressX
                    diffOG = diff*(imgW/scrnx)
                elif firstPress == True and secondPress == True and thirdPress == True:
                    fourthPress = True
                    return abs(diffOG*scalefactor)
            if event.type == pg.QUIT: # Checks if the user has pressed the close (X) button or pressed alt + F4
                sys.exit()
            if event.type == pg.K_ESCAPE:
                firstPress == False
                secondPress == False
        pg.event.pump()
        

base_path = os.getcwd()  # Get the current working directory
print(base_path)
image_dir = "Images"  # Relative path to the image directory
lst = os.listdir(os.path.join(base_path, image_dir))
number_files = len(lst)


for i in range (number_files - 1):
    distance = display_image(str(base_path)+"/Images/1 ("+str(i+1)+").jpg")

