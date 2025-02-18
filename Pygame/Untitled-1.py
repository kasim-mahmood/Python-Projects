import pygame

pygame.init()

dis_width = 600
dis_height = 600
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    
pygame.draw.circle(canvas,(0,0,255),[100,100],50,2)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False