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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            pygame.draw.circle(canvas,(0,255,0),[x,y],100,0)

        if event.type == pygame.KEYDOWN:
            print('A key has been pressed')

            if event.key == pygame.K_LEFT:
                print('The left key has been pressed')

            if event.key == pygame.K_a:
                print('The a key has been pressed')

            if event.key == pygame.K_RIGHT:
                print('The right key has been pressed')

            if event.key == pygame.K_c:
                print('The c key has been pressed')

            if event.key == pygame.K_g:
                print('The g key has been pressed')

            if event.key == pygame.K_f:
                print('The f key has been pressed')

            if event.key == pygame.K_e:
                print('The e key has been pressed')

            if event.key == pygame.K_d:
                pygame.draw.rect(canvas,(0,0,255),[100,250,400,100],0)
            


    pygame.display.update()
