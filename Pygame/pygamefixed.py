import pygame


pygame.init()

background_color = (251, 253, 138)

window_height = 400
window_width = 500

canvas = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game by AKC')
quit = False


while quit == False:
    canvas.fill(background_color)
    pygame.draw.circle(canvas,(0,0,255),[100,100],50,2)

    pygame.draw.rect(canvas,(0,0,255),
                 [100,250,400,100],0)

    #Set a back ground image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    #Set a background color
    
    pygame.display.update()