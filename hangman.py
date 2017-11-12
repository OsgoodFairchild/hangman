import pygame as pg

from gallow import Gallow
from man import Man
from settings import Settings
import game_function as gf

def run_game():

    pg.init()

    gallow = Gallow()
    man = Man()
    settings = Settings()

    screen = pg.display.set_mode((settings.screen_width,
                                        settings.screen_height))
    pg.display.set_caption("Hangman")

    while True:
        for event in pg.event.get():
            gf.check_events(event)

        screen.fill(settings.screen_color)

        answer = "HELLO"

        string = ""

        gf.print_empty_game_board(screen)
        man.draw_entire_man(screen)
        gallow.draw_structure(screen)

        pg.display.flip()




run_game()
