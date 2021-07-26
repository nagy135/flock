import pygame
from constants import *

class Bird:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, display):
        pygame.draw.polygon(display, black, [[100, 100], [0, 200], [200, 200]], 5)
