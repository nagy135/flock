import pygame
import time
import random
import copy

from bird import Bird
from constants import *
from utils import euclidean_distance

class Flock:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flock')
        self.clock = pygame.time.Clock()
        self.tick_time = time.time()

        self.toggle_interaction_distance = True

        self.toggle_rule_align = True
        self.toggle_rule_avoid = False
        self.toggle_rule_center = False

        self.birds = []
        for _ in range(BIRD_COUNT):
            self.birds.append(
                    Bird(
                        random.randint(0, WIDTH),
                        random.randint(0, HEIGHT),
                        random.randint(0, 359),
                        )
                    )

    def draw(self):
        for bird in self.birds:
            bird.draw(self.display, self.toggle_interaction_distance)

    def tick(self):
        now = time.time()
        if abs(self.tick_time - now) > TIME_STEP_SIZE:
            self.tick_time = now

            if self.toggle_rule_align:
                self.rule_align()
            if self.toggle_rule_avoid:
                self.rule_avoid()
            if self.toggle_rule_center:
                self.rule_center()

            self.move()

    def rule_align(self):
        copies = copy.deepcopy(self.birds)
        for bird in self.birds:
            angles_in_range = []
            for bird2 in copies:
                if bird is not bird2 and euclidean_distance(bird.x, bird2.x, bird.y, bird2.y) <= BIRD_INTERACTION_DISTANCE:
                    angles_in_range.append(bird2.angle)
            if angles_in_range:
                average = sum(angles_in_range) // len(angles_in_range)
                if bird.angle > average:
                    bird.angle -= ALIGN_DELTA_ANGLE
                elif bird.angle < average:
                    bird.angle += ALIGN_DELTA_ANGLE
                bird.angle %= 360



    def rule_avoid(self):
        pass

    def rule_center(self):
        pass

    def move(self):
        for bird in self.birds:
            bird.move()

    def start(self):
        self.end = False
        pause = False
        while not self.end:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        pause = not pause
                    if event.key == pygame.K_r:
                        self.__init__()
                    if event.key == pygame.K_1:
                        self.toggle_rule_align = not self.toggle_rule_align
                    if event.key == pygame.K_2:
                        self.toggle_rule_avoid = not self.toggle_rule_avoid
                    if event.key == pygame.K_3:
                        self.toggle_rule_center = not self.toggle_rule_center

                    if event.key == pygame.K_4:
                        self.toggle_interaction_distance = not self.toggle_interaction_distance
                    if event.key == pygame.K_q:
                        self.end = True
                if event.type == pygame.QUIT:
                    self.end = True
            if not pause:
                self.tick()
            self.display.fill(white)
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    a = Flock()
    a.start()
