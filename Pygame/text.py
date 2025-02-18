import pygame ## Imports pygame library

pygame.init() ## Activates pygame

dis_width = 640 ## Sets the width of the window
dis_height = 480 ## Sets the hight of the window
color = (255,255,255) 
canvas = pygame.display.set_mode((dis_width, dis_height)) ## Creates the canvas/screen for the window
clock = pygame.time.Clock()
CHANGE_COLOR = pygame.USEREVENT + 1 # Creates a custom event

pygame.display.set_caption('Snake Game by AKC') ## Sets the caption of the window
    
font = pygame.font.SysFont("comicsansms",72)
text = font.render("",True,(0,128,0))
letters = ""
running = True ## Variable always set to true while the window is open

while running: ## The main parts of the game in this while loop

    for event in pygame.event.get(): ## Detects when an event is happening
        if event.type == pygame.QUIT: ## Checks if the event is QUIT
            running = False ## Stops the game
        
   
        if event.type == pygame.KEYDOWN: ## Checks if a key is pressed

            if event.key == pygame.K_a: ## Checks if the key '1' is pressed
             letters = letters + "a"

            elif event.key == pygame.K_b: ## Checks if the key '1' is pressed
                letters = letters + "b"

            elif event.key == pygame.K_c: ## Checks if the key '1' is pressed
                letters = letters + "c"

            elif event.key == pygame.K_d: ## Checks if the key '1' is pressed
             letters = letters + "d"

            elif event.key == pygame.K_e: ## Checks if the key '1' is pressed
             letters = letters + "e"

            elif event.key == pygame.K_f: ## Checks if the key '1' is pressed
             letters = letters + "f"

            elif event.key == pygame.K_g: ## Checks if the key '1' is pressed
             letters = letters + "g"

            elif event.key == pygame.K_h: ## Checks if the key '1' is pressed
             letters = letters + "h"

            elif event.key == pygame.K_i: ## Checks if the key '1' is pressed
             letters = letters + "i"

            elif event.key == pygame.K_j: ## Checks if the key '1' is pressed
             letters = letters + "j"

            elif event.key == pygame.K_k: ## Checks if the key '1' is pressed
             letters = letters + "k"

            elif event.key == pygame.K_l: ## Checks if the key '1' is pressed
             letters = letters + "l"

            elif event.key == pygame.K_m: ## Checks if the key '1' is pressed
             letters = letters + "m"

            elif event.key == pygame.K_n: ## Checks if the key '1' is pressed
             letters = letters + "n"

            elif event.key == pygame.K_o: ## Checks if the key '1' is pressed
             letters = letters + "o"

            elif event.key == pygame.K_p: ## Checks if the key '1' is pressed
             letters = letters + "p"

            elif event.key == pygame.K_q: ## Checks if the key '1' is pressed
             letters = letters + "q"

            elif event.key == pygame.K_r: ## Checks if the key '1' is pressed
             letters = letters + "r"

            elif event.key == pygame.K_s: ## Checks if the key '1' is pressed
             letters = letters + "s"

            elif event.key == pygame.K_t: ## Checks if the key '1' is pressed
             letters = letters + "t"

            elif event.key == pygame.K_u: ## Checks if the key '1' is pressed
             letters = letters + "u"

            elif event.key == pygame.K_v: ## Checks if the key '1' is pressed
             letters = letters + "v"

            elif event.key == pygame.K_w: ## Checks if the key '1' is pressed
             letters = letters + "w"

            elif event.key == pygame.K_x: ## Checks if the key '1' is pressed
             letters = letters + "x"

            elif event.key == pygame.K_y: ## Checks if the key '1' is pressed
             letters = letters + "y"

            elif event.key == pygame.K_z: ## Checks if the key '1' is pressed
             letters = letters + "z"

            elif event.key == pygame.K_SPACE: ## Checks if the key '1' is pressed
             letters = letters + " "

            

     
        text = font.render(letters,True,(0,128,0))
        canvas.fill(color)
        canvas.blit(text,(320 - text.get_width() // 2,240 - text.get_height() // 2))
 
 
 

    pygame.display.update() ## Updaes the display
    clock.tick(96)
