import pygame ## Imports pygame library
import time

pygame.init() ## Activates pygame

dis_width = 640 ## Sets the width of the window
dis_height = 480 ## Sets the hight of the window
color = (255,255,255) 
canvas = pygame.display.set_mode((dis_width, dis_height)) ## Creates the canvas/screen for the window
clock = pygame.time.Clock()
CHANGE_COLOR = pygame.USEREVENT + 1 # Creates a custom event

pygame.display.set_caption('Snake Game by AKC') ## Sets the caption of the window
    
font = pygame.font.SysFont("comicsansms",72)
text = font.render("",True,(0,128,0))
letters = ""
running = True ## Variable always set to true while the window is open
num = 11
COUNTDOWN = pygame.USEREVENT + 1
pos = 310 
pygame.time.set_timer(COUNTDOWN, 1000)

while running: ## The main parts of the game in this while loop
    pygame.draw.circle(canvas,(0,255,0),[320,240],50,3)

    pygame.draw.circle(canvas,(0,255,0),[320,240],60,3)

    pygame.draw.line(canvas,(0,255,0), (520, 240), (130, 240),2)
    pygame.draw.line(canvas,(0,255,0), (315, 340), (315, 130),2)
    for event in pygame.event.get(): ## Detects when an event is happening
        if event.type == pygame.QUIT: ## Checks if the event is QUIT
            running = False ## Stops the game

    

        if event.type == COUNTDOWN:
            if num != 0:
                num = num - 1
                print(str(num))
                text = font.render(str(num),True,(0,128,0))
                canvas.fill((255,255,255))
                canvas.blit(text,(320 - text.get_width() // 2,240 - text.get_height() // 2))
                pygame.draw.line(canvas,(0,255,0), (315, 220), (pos, 180),2)
                pos = pos + 50

                


    pygame.display.update() ## Updaes the display
    clock.tick(96)