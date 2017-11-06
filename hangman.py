import pygame, sys

def run_game():

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption("Hangman")

    background_color = 230, 230, 230

    black = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(background_color)

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('HANGMAN', True, (0, 0, 0))
        screen.blit(textsurface,(650,25))


        pygame.draw.lines(screen, black, False, [(700,250), (700,150),
         (1000,150), (1000, 550), (850, 550), (1150, 550)], 4)

        pygame.draw.circle(screen, black, (700, 300), 50, 4)



        pygame.display.flip()

run_game()
