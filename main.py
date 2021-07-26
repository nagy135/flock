import pygame
import time

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
WIDTH = 1000
HEIGHT = 1000
TIME_STEP_SIZE = 0.5

class Flock(object):

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Marbles')
        self.clock = pygame.time.Clock()
        self.tick_time = time.time()

    def draw(self):
        pygame.draw.polygon(self.display, black, [[100, 100], [0, 200], [200, 200]], 5)

    def tick(self):
        now = time.time()
        if abs(self.tick_time - now) > TIME_STEP_SIZE:
            self.tick_time = now
            self.move()

    def move(self):
        pass

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
                    if event.key == pygame.K_q:
                        self.end = True
                if event.type == pygame.QUIT:
                    self.end = True
            if not pause:
                self.tick()
            self.display.fill(white)
            self.tick()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    a = Flock()
    a.start()
