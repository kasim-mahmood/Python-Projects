import pygame

pygame.init()

dis_width = 750
dis_height = 600
color = (255, 255, 255)
canvas = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by AKC')
    
xpos = 100

image = [pygame.image.load('download.jpg'),pygame.image.load('download (1).jpg'),pygame.image.load('download (2).jpg'),pygame.image.load('download (3).jpg'),pygame.image.load('download (4).jpg')]
imagenum = 0
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        if event.type == pygame.KEYDOWN:
            print('A key has been pressed')

            if event.key == pygame.K_LEFT:
                canvas.blit(image[imagenum], dest = (0,0))
                imagenum = imagenum - 1
                if imagenum == 0:
                    imagenum = 4
            if event.key == pygame.K_RIGHT:
                canvas.blit(image[imagenum], dest = (0,0))
                if imagenum != 5:
                    imagenum = imagenum + 1
                else:
                    imagenum = 0
                if imagenum == 5:
                    imagenum = 0



            


        pygame.display.update()
