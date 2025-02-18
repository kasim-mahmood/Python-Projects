import pygame ## Imports pygame library

pygame.init() ## Activates pygame

dis_width = 750 ## Sets the width of the window
dis_height = 600 ## Sets the hight of the window
color = (255,255,255) 
canvas = pygame.display.set_mode((dis_width, dis_height)) ## Creates the canvas/screen for the window

pygame.display.set_caption('Snake Game by AKC') ## Sets the caption of the window
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
CHANGE_COLOR = pygame.USEREVENT + 1
bgcolor = BLACK
pygame.time.set_timer(CHANGE_COLOR, 2000)
running = True # Variable always set to true while the window is open

while running: # The main parts of the game in this while loop

    for event in pygame.event.get():
        if event.type == CHANGE_COLOR:
            if bgcolor == BLACK:
                canvas.fill(BLACK)
                bgcolor = GREEN
            elif bgcolor == GREEN:
                canvas.fill(GREEN)
                bgcolor = WHITE

            elif bgcolor == WHITE:
                canvas.fill(WHITE)
                bgcolor = BLACK
                
    
        if event.type == pygame.QUIT: ## Checks if the event is QUIT
            running = False ## Stops the game
    pygame.display.update() ## Updaes the display
pygame.quit()