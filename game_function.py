import pygame, sys
import pygame.font


def check_events(event):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()

def print_title(screen):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    game_title = myfont.render('HANGMAN', True, (0, 0, 0))
    screen.blit(game_title,(650,25))

def print_empty_game_board(screen):
    myfont = pygame.font.SysFont('Comic Sans MS', 75)
    answer = "HELLO"
    game_board = myfont.render("_", True, (0 ,0, 0))
    screen.blit(game_board, (500, 600))
