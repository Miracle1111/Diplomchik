import pygame

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
red = (255, 0, 0)

# crashed = False
# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        mouse = pygame.mouse.get_pos()


        # print(mouse)

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, red, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))

        pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
        pygame.display.update()


game_intro()