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

    pygame.draw.polygon(canvas, (255,0,0), [[200,200],[250,150],[300,200]],0)
    pygame.draw.polygon(canvas, (255,0,0), [[500,300],[600,300],[600,500],[500,500]],0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
