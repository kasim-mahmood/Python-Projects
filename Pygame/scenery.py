import pygame

pygame.init()

dis_width = 750
dis_height = 600
color = (173, 216, 230)
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    
xpos = 100


running = True
while running:
    canvas.fill(color)

    pygame.draw.rect(canvas, (196, 164, 132),[1,500,1000,200],0)
    pygame.draw.rect(canvas, (196, 164, 132),[150,400,25,400],0)

    pygame.draw.polygon(canvas, (0,255,0), [[110,400],[160,350],[210,400]],0)
    pygame.draw.polygon(canvas, (0,255,0), [[110,425],[160,375],[210,425]],0)

    pygame.draw.circle(canvas,(255, 213, 128),[500,200],60,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
