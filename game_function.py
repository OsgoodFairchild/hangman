import pygame, sys


def check_events(event):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()

def print_title(screen):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    game_title = myfont.render('HANGMAN', True, (0, 0, 0))
    screen.blit(game_title,(650,25))
