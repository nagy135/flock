import pygame

from constants import *

class Bird:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, display):
        pygame.draw.polygon(
                display,
                black,
                [
                    [self.x - BIRD_WIDTH, self.y + BIRD_SIZE],
                    [self.x + BIRD_WIDTH, self.y + BIRD_SIZE],
                    [self.x, self.y - BIRD_SIZE],
                    [self.x - BIRD_WIDTH, self.y + BIRD_SIZE]
                ],
                2)
