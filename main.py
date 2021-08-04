import pygame
import time
import random
import copy

from bird import Bird
from constants import *
from utils import *

class Flock:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flock')
        self.clock = pygame.time.Clock()
        self.tick_time = time.time()

        self.interaction_delta = 0

        self.toggle_interaction_distance = True
        self.toggle_bird_debug = True

        self.toggle_rule_align = True
        self.toggle_rule_avoid = False
        self.toggle_rule_center = False

        self.random_initialization()

    def random_initialization(self):
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
            bird.draw(self.display, self)
        textsurface = BIRD_DEBUG_FONT.render(f"{len(self.birds)}", False, black)
        self.display.blit(textsurface,(5,5))

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
        for (i, bird) in enumerate(self.birds):
            angles_in_range = []
            for (n, bird2) in enumerate(copies):
                if i != n and euclidean_distance(bird.x, bird.y, bird2.x, bird2.y) <= BIRD_INTERACTION_DISTANCE+self.interaction_delta:
                    angles_in_range.append(bird2.angle)
            if angles_in_range:
                average_x, average_y = vector_average_angle(angles_in_range)

                self_x = math.cos(math.radians(bird.angle))
                self_y = math.sin(math.radians(bird.angle))

                self_x += average_x * ALIGN_CHANGE_CONSTANT
                self_y += average_y * ALIGN_CHANGE_CONSTANT

                tangle = round(math.degrees(math.atan2(self_y, self_x)))
                if tangle < 0:
                    bird.angle = 360 + tangle
                else:
                    bird.angle = tangle

    def change_flock_size(self, change):
        if change > 0:
            for _ in range(change):
                self.birds.append(
                        Bird(
                            random.randint(0, WIDTH),
                            random.randint(0, HEIGHT),
                            random.randint(0, 359),
                            )
                        )
        else:
            self.birds = self.birds[:change]


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
                    if event.key == pygame.K_i:
                        self.random_initialization()
                    if event.key == pygame.K_1:
                        self.toggle_rule_align = not self.toggle_rule_align
                    if event.key == pygame.K_2:
                        self.toggle_rule_avoid = not self.toggle_rule_avoid
                    if event.key == pygame.K_3:
                        self.toggle_rule_center = not self.toggle_rule_center

                    if event.key == pygame.K_4:
                        self.toggle_interaction_distance = not self.toggle_interaction_distance
                    if event.key == pygame.K_5:
                        self.toggle_bird_debug = not self.toggle_bird_debug
                    if event.key == pygame.K_q:
                        self.end = True

                    if event.key == pygame.K_k:
                        self.change_flock_size(1)
                    if event.key == pygame.K_j:
                        self.change_flock_size(-1)

                    if event.key == pygame.K_h:
                        self.interaction_delta -= 5
                    if event.key == pygame.K_l:
                        self.interaction_delta += 5

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
