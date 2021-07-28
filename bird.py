import pygame
import math

from constants import *
from utils import rotate_point

class Bird:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, display):
        p1 = self.rotate_point_around_center((self.x - BIRD_WIDTH, self.y + BIRD_SIZE))
        p2 = self.rotate_point_around_center((self.x + BIRD_WIDTH, self.y + BIRD_SIZE))
        p3 = self.rotate_point_around_center((self.x, self.y - BIRD_SIZE))
        pygame.draw.polygon(
                display,
                black,
                [p1, p2, p3, p1],
                2)

    def rotate_point_around_center(self, point):
        return rotate_point((self.x, self.y), point, self.angle)

    def move(self):
        self.x += math.sin(math.radians(self.angle)) * STEP_SIZE;
        self.y -= math.cos(math.radians(self.angle)) * STEP_SIZE;

        self.x %= WIDTH
        self.y %= HEIGHT
