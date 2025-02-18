## How to pygame.


import pygame ## Imports pygame library

pygame.init() ## Activates pygame

dis_width = 750 ## Sets the width of the window
dis_height = 600 ## Sets the hight of the window
color = (255,255,255) 
canvas = pygame.display.set_mode((dis_width, dis_height)) ## Creates the canvas/screen for the window

CHANGE_COLOR = pygame.USEREVENT + 1 # Creates a custom event

font = pygame.font.SysFont("comicsansms",72) # Sets a font for the text
text = font.render("Hello world",True,(0,128,0)) # Sets the text and text color
canvas.blit(text,(320 - text.get_width() // 2,240 - text.get_height() // 2)) # Displays the text
  

pygame.display.set_caption('Snake Game by AKC') ## Sets the caption of the window
    
pygame.time.set_timer(CHANGE_COLOR, 2000) # Creates a timer thagt ctivates an vent (In ms)


running = True ## Variable always set to true while the window is open

while running: ## The main parts of the game in this while loop

 #   canvas.fill(color) # Changes the background colour

 #   pygame.draw.rect(canvas,[100,250,100,100],0) ## Draws a rectangle/square

    pygame.draw.circle(canvas,(0,255,0),[10,10],50,3) ## Draws a circle

    for event in pygame.event.get(): ## Detects when an event is happening
        if event.type == pygame.QUIT: ## Checks if the event is QUIT
            running = False ## Stops the game

        if event.type == pygame.KEYDOWN: ## Checks if a key is pressed
            if event.key == pygame.K_1: ## Checks if the key '1' is pressed
                print("The key 1 has been pressed.") ## Fulfills an line of code after it is pressed
                canvas.blit(text,(320 - text.get_width() // 2,240 - text.get_height() // 2)) # Shows the text

        if event.type == pygame.MOUSEBUTTONDOWN: # Checks if the mouse button was pressed
            mousepos = pygame.mouse.get_pos() # Saves the mouse position

        if event.type == CHANGE_COLOR: # Detects the custom event (Line 13)
            print('Custom event activted')

        # canvas.blit(image, dest = (0,0)) Adds an image to the screen

    pygame.display.update() # Updaes the display
