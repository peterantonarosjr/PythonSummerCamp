# Importing pygame and using all functions available to us
import pygame
from pygame import *

#Initialize pygame
pygame.init()

#Create window
GAME_WINDOW = display.set_mode((900,400))
display.set_caption('Attack of the Vampire Pizzas!')

#Main Game Loop
game_running = True

while game_running:

    #Get all events (things a user is doing in the pygame window)
    for event in pygame.event.get():

        #If the event type is QUIT then we stop the loop and exit
        if event.type == QUIT:
            game_running = False

        #Always update the display
        display.update()

#Quit and close the window
pygame.quit()
