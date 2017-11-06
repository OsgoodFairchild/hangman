import pygame

class Man():
    """ A class to store the man from hangman"""

    def __init__(self):
        self.line_color = 0, 0, 0





    def draw_head(self, screen):
        pygame.draw.circle(screen, self.line_color, (700, 300), 50, 4)


    def draw_neck(self, screen):
        pygame.draw.lines(screen, self.line_color, False, [(700, 350),
                                                        (700, 400)], 4)

    def draw_right_arm(self, screen):
        pygame.draw.lines(screen, self.line_color, False, [(800, 350),
                                                        (700, 400)], 4)

    def draw_left_arm(self, screen):
        pygame.draw.lines(screen, self.line_color, False, [(600, 350),
                                                        (700, 400)], 4)

    def draw_body(self, screen):
        pygame.draw.lines(screen, self.line_color, False, [(700, 400),
                                                        (700, 500)], 4)
    def draw_right_leg(self, screen):
        pygame.draw.lines(screen, self.line_color, False, [(700, 500),
                                                        (800, 550)], 4)
    def draw_left_leg(self, screen):
        pygame.draw.lines(screen, self.line_color, False, [(700, 500),
                                                        (600, 555)], 4)
