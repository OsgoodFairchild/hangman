import pygame

class Man():
    """ A class to store the man from hangman"""

    def __init__(self):
        self.line_color = 0, 0, 0
        self.head = (700, 300)
        self.left_eye = (685, 285)
        self.right_eye = (715, 285)
        self.neck = [(700, 350), (700, 400)]
        self.right_arm = [(800, 350), (700, 400)]
        self.left_arm = [(600, 350), (700, 400)]
        self.body = [(700, 400), (700, 500)]
        self.right_leg = [(700, 500), (800, 550)]
        self.left_leg = [(700, 500), (600, 555)]

    def draw_head(self, screen):
        pygame.draw.circle(screen, self.line_color, self.head, 50, 4)
        pygame.draw.circle(screen, self.line_color, self.left_eye, 5, 2)
        pygame.draw.circle(screen, self.line_color, self.right_eye, 5, 2)

    def draw_neck(self, screen):
        pygame.draw.lines(screen, self.line_color, False, self.neck, 4)

    def draw_right_arm(self, screen):
        pygame.draw.lines(screen, self.line_color, False, self.right_arm, 4)

    def draw_left_arm(self, screen):
        pygame.draw.lines(screen, self.line_color, False, self.left_arm, 4)

    def draw_body(self, screen):
        pygame.draw.lines(screen, self.line_color, False, self.body, 4)

    def draw_right_leg(self, screen):
        pygame.draw.lines(screen, self.line_color, False, self.right_leg, 4)

    def draw_left_leg(self, screen):
        pygame.draw.lines(screen, self.line_color, False, self.left_leg, 4)

    def draw_entire_man(self, screen):
        self.draw_head(screen)
        self.draw_neck(screen)
        self.draw_right_arm(screen)
        self.draw_left_arm(screen)
        self.draw_body(screen)
        self.draw_left_leg(screen)
        self.draw_right_leg(screen)
