import pygame

pygame.init()

color = (255, 255, 255)
canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Snake Game by AKC')
    


running = True
while running:
    canvas.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    pygame.display.update()
