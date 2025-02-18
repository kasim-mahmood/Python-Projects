import pygame

pygame.init()

dis_width = 750
dis_height = 600
color = (0, 0, 0)
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    
xpos = 100


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                canvas.fill((255,0,0))

            elif event.key == pygame.K_g:
                canvas.fill((0,255,0))

            elif event.key == pygame.K_b:
                canvas.fill((0,0,255))

            elif event.key == pygame.K_SPACE:
                canvas.fill((255,255,255))
            
            else:
                canvas.fill((0,0,0))



    pygame.display.update()
