# Importing pygame and using all functions available to us
import pygame
from pygame import *

#Initialize pygame
pygame.init()

#Constant variables----------------------------------------
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH,WINDOW_HEIGHT)

#Tile parameters
WIDTH = 100
HEIGHT = 100

#Define Colors
WHITE = (255,255,255)

#Create window---------------------------------------------
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')

#Load Assets-----------------------------------------------
#Setup the background
bg_img = image.load('gameassets/restaurant.jpg')
bg_surf = Surface.convert_alpha(bg_img)
BACKGROUND = transform.scale(bg_surf,WINDOW_RES)

#Setup the vampire pizza
pizza_img = image.load('gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf,(WIDTH,HEIGHT))

#Setup the project classes---------------------------------
class Monster(object):
    eats = 'food'
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name+"speaks")

    def eat(self,meal):
        if meal == self.eats:
            print("YUM")
        else:
            print("Blech!")

#Initialize and draw the background grid-------------------
tile_color = WHITE
#draw.rect(BACKGROUND,tile_color,(0,0,WIDTH,HEIGHT),1)
#Loop to draw the background grid
for row in range(6):
    draw.rect(BACKGROUND, tile_color, (0, HEIGHT * row, WIDTH, HEIGHT), 1)
    for column in range(11):
        draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)

#Display Assets--------------------------------------------
#Display the background to the screen
GAME_WINDOW.blit(BACKGROUND,(0,0))

#Display the vampire pizza to the screen
GAME_WINDOW.blit(VAMPIRE_PIZZA,(150,150))

#Test drawing shapes to the screen-------------------------
#draw.circle(GAME_WINDOW,(255,0,0),(925,425),25,0)
#draw.rect(GAME_WINDOW,(0,0,255),(25,25,50,25),0)

#Main Game Loop---------------------------------------------------
game_running = True

while game_running:

    #Get all events (things a user is doing in the pygame window)
    for event in pygame.event.get():

        #If the event type is QUIT then we stop the loop and exit
        if event.type == QUIT:
            game_running = False

        #Always update the display
        display.update()
#-----------------------------------------------------------------
#Quit and close the window
pygame.quit()
