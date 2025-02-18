import pygame

pygame.init()

dis_width = 750
dis_height = 600
color = (255,255,255)
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    
xpos = 100


running = True
while running:
    canvas.fill(color)
    for i in range (0,6):
        xpos = xpos + 50
        pygame.draw.rect(canvas,(255,0,0),
                 [100,250,100,100],0)
        pygame.draw.rect(canvas,(255,0,0),
                 [200,250,100,100],1)
        pygame.draw.rect(canvas,(255,0,0),
                 [300,250,100,100],0)
        pygame.draw.rect(canvas,(255,0,0),
                 [400,250,100,100],1)
        pygame.draw.rect(canvas,(255,0,0),
                 [500,250,100,100],0)
        pygame.draw.rect(canvas,(255,0,0),
                 [600,250,100,100],1)
        

        pygame.draw.rect(canvas,(255,0,0),
                 [100,400,100,100],0)
        pygame.draw.rect(canvas,(255,0,0),
                 [200,400,100,100],1)
        pygame.draw.rect(canvas,(255,0,0),
                 [100,500,100,100],1)
        pygame.draw.rect(canvas,(255,0,0),
                 [200,500,100,100],0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
