import pygame

class Gallow():

    """A class for the gallow in hangman game"""

    def __init__(self):

        self.line_color = 0, 0, 0
        self.structure = [(700,250), (700,150),
         (1000,150), (1000, 550), (850, 550), (1150, 550)]

    def draw_structure(self, screen):
        pygame.draw.lines(screen, self.line_color, False, self.structure, 4)
