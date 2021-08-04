from pygame import gfxdraw
import pygame
import math
import random

from constants import *
from utils import rotate_point

class Bird:

    def __repr__(self):
        return f"({int(self.x)},{int(self.y)}), °{self.angle}"

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, display, flock):
        p1 = self.rotate_point_around_center((self.x - BIRD_WIDTH, self.y + BIRD_SIZE))
        p2 = self.rotate_point_around_center((self.x + BIRD_WIDTH, self.y + BIRD_SIZE))
        p3 = self.rotate_point_around_center((self.x, self.y - BIRD_SIZE))

        if flock.toggle_interaction_distance:
            pygame.draw.circle(
                    display,
                    red,
                    (self.x, self.y),
                    BIRD_INTERACTION_DISTANCE + flock.interaction_delta,
                    1
                    )
        gfxdraw.filled_polygon(
                display,
                [p1, p2, p3, p1],
                black
                )

        if flock.toggle_bird_debug:
            textsurface = BIRD_DEBUG_FONT.render(f"({int(self.x)},{int(self.y)}), °{self.angle}", False, red)
            display.blit(textsurface,(self.x, self.y - 3))

    def rotate_point_around_center(self, point):
        return rotate_point((self.x, self.y), point, self.angle)

    def move(self):
        self.x += math.sin(math.radians(self.angle)) * STEP_SIZE;
        self.y -= math.cos(math.radians(self.angle)) * STEP_SIZE;

        self.x %= WIDTH
        self.y %= HEIGHT

        if not random.randint(0, RANDOM_ROTATE_CHANGE - 1):
            self.angle += random.randint(-RANDOM_ROTATE, RANDOM_ROTATE)
