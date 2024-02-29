#from Image_legnth_manual import display_image
import pygame as pg 
import sys

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
font1 = pg.font.SysFont('Arial', 40)


def display_image(image_path):
    image = pg.image.load(image_path)
    imageScale = image.get_height()/image.get_width()
    image = pg.transform.scale(image, (scrnx, scrnx*imageScale))
    firstPress = False
    firstPressX = float()
    secondPress = False
    secondPressX = float()
    thirdPress = False
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
            screen.blit(confirmation, (200,500))
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
                    thirdPress == True
            if event.type == pg.QUIT: # Checks if the user has pressed the close (X) button or pressed alt + F4
                sys.exit()
            if event.type == pg.K_ESCAPE:
                firstPress == False
                secondPress == False
        pg.event.pump()

#for i in range (2):
distance = display_image("Test1"+".png")
image_width = 5852  # Width of the image in pixels
scale_factor = 0.5  # Scale factor for the distance calculation
