import pygame
import random

pygame.init()

dis_width = 750
dis_height = 600
color = (255,255,255)
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    
xpos = 100

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)

            x,y = pygame.mouse.get_pos()
            pygame.draw.circle(canvas,(r,g,b),[x,y],50,3)

    pygame.display.update()
