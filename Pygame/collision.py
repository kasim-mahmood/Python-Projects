import pygame ## Imports pygame library
import random
pygame.init() ## Activates pygame
dis_width = 750 ## Sets the width of the window
dis_height = 600 ## Sets the hight of the window
color = (255,255,255) 
canvas = pygame.display.set_mode((dis_width, dis_height)) ## Creates the canvas/screen for the window
y = 250
x = 400
x1 = random.randint(0,750)
score = 0
y1 = random.randint(0,600)
pygame.display.set_caption('Snake Game by AKC') ## Sets the caption of the window
rec1 = pygame.draw.rect(canvas,(255,0,0),[100,250,100,100],0)
rec2 = pygame.draw.rect(canvas,(255,0,0),[400,250,100,100],0)
font = pygame.font.SysFont("comicsansms",72)
text = font.render(str(score),True,(0,128,0))
running = True ## Variable always set to true while the window is open

while running: ## The main parts of the game in this while loop

    canvas.blit(text,(320 - text.get_width() // 2,240 - text.get_height() // 2))


    for event in pygame.event.get(): ## Detects when an event is happening
        collide = rec1.colliderect(rec2)
        if event.type == pygame.QUIT: ## Checks if the event is QUIT
            running = False ## Stops the game

        if event.type == pygame.KEYDOWN: ## Checks if a key is pressed
            if event.key == pygame.K_w: ## Checks if the key '1' is pressed
                y = y - 10

            if event.key == pygame.K_s: ## Checks if the key '1' is pressed
                y = y + 10

            if event.key == pygame.K_a: ## Checks if the key '1' is pressed
                x = x - 10

            if event.key == pygame.K_d: ## Checks if the key '1' is pressed
                x = x + 10
        canvas.fill(color)
        rec1 = pygame.draw.rect(canvas,(255,0,0),[x1,y1,75,75],0)
        rec2 = pygame.draw.rect(canvas,(255,0,0),[x,y,100,100],0)
        

        if (collide):
            score = score + 1
            text = font.render(str(score),True,(0,128,0))
            canvas.blit(text,(320 - text.get_width() // 2,240 - text.get_height() // 2))
    canvas.blit(text,(320 - text.get_width() // 2,240 - text.get_height() // 2))

    pygame.display.update() # Updaes the display
