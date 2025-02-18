import pygame

pygame.init()

dis_width = 750
dis_height = 600
color = (255,255,255)
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    



running = True
while running:
    canvas.fill(color)

    # Olympic
    pygame.draw.circle(canvas,(0,0,255),[150,100],100,8)
    pygame.draw.circle(canvas,(255,255,0),[250,200],100,8)
    pygame.draw.circle(canvas,(0,0,0),[350,100],100,8)
    pygame.draw.circle(canvas,(0,255,0),[450,200],100,8)
    pygame.draw.circle(canvas,(255,0,0),[550,100],100,8)

    pygame.draw.circle(canvas,(255,0,0),[500,400],160,8)
    pygame.draw.circle(canvas,(255,165,0),[500,400],150,8)
    pygame.draw.circle(canvas,(255,255,204),[500,400],140,8)
    pygame.draw.circle(canvas,(0,255,0),[500,400],130,8)
    pygame.draw.circle(canvas,(173,216,230),[500,400],120,8)
    pygame.draw.circle(canvas,(0,0,255),[500,400],110,8)
    pygame.draw.circle(canvas,(160,32,240),[500,400],100,8)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()