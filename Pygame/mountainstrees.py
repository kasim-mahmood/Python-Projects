import pygame

pygame.init()

dis_width = 750
dis_height = 600
color = (255, 255, 255)
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    
xpos = 100


running = True
while running:
    canvas.fill(color)

    pygame.draw.rect(canvas, (0, 0, 255),[1,1,1000,200],0)

    pygame.draw.circle(canvas,(255, 213, 128),[400,140],60,0)

    treex1 = 130
    treex2 = 160
    treex3 = 210
    stem = 150

    for i in range(0,4):
        pygame.draw.rect(canvas, (196, 164, 132),[stem,400,25,400],0)
        pygame.draw.polygon(canvas, (0,255,0), [[treex1,400],[treex2,350],[treex3,400]],0)
        pygame.draw.polygon(canvas, (0,255,0), [[treex1,425],[treex2,350],[treex3,425]],0)
        stem = stem + 150
        treex1 = treex1 + 150
        treex2 = treex2 + 150
        treex3 = treex3 + 150

    x1 = 600
    x2 = 700
    x3 = 800
    
    for i in range(0,5):
        pygame.draw.polygon(canvas, (150,75,0), [[x1,200],[x2,100],[x3,200]],0)
        x1 = x1 - 150
        x2 = x2 - 150
        x3 = x3 - 150

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
