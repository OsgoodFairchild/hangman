import pygame

from gallow import Gallow
from man import Man
from settings import Settings
import game_function as gf

def run_game():

    pygame.init()
    pygame.font.init()

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

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('HANGMAN', True, (0, 0, 0))
        screen.blit(textsurface,(650,25))

        gallow.draw_structure(screen)
        man.draw_head(screen)
        man.draw_neck(screen)
        man.draw_right_arm(screen)
        man.draw_left_arm(screen)
        man.draw_body(screen)
        man.draw_left_leg(screen)
        man.draw_right_leg(screen)



        pygame.display.flip()

run_game()
