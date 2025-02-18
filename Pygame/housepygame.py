import pygame

pygame.init()

color = (255, 255, 255)
canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Snake Game by AKC')
    


running = True
while running:
    canvas.fill(color)

    pygame.draw.rect(canvas,(34,139,34),
                 [0,400,500,100],0)

    pygame.draw.rect(canvas,(173, 216, 230),
                 [0,0,500,400],0)
    
    pygame.draw.rect(canvas,(255,255,204),
                 [200,150,300,300],0)

    pygame.draw.rect(canvas,(31, 81, 255),
                 [225,200,100,100],0)
    
    pygame.draw.rect(canvas,(31, 81, 255),
                 [425,200,100,100],0)

    pygame.draw.rect(canvas,(165, 42, 42),
                 [300,350,75,110],0)

    pygame.draw.polygon(canvas, (255,0,0), (225 255, 300 300, 425 425))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    pygame.display.update()
