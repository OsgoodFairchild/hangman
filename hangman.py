import pygame

from gallow import Gallow
from man import Man
from settings import Settings
import game_function as gf

def run_game():

    pygame.init()

    gallow = Gallow()
    man = Man()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width,
                                        settings.screen_height))
    pygame.display.set_caption("Hangman")

    while True:
        for event in pygame.event.get():
            gf.check_events(event)

        screen.fill(settings.screen_color)

        pygame.display.flip()




run_game()
