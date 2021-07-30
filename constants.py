import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)

WIDTH = 1000
HEIGHT = 1000
TIME_STEP_SIZE = 0.01 # global tick size

BIRD_COUNT = 200
BIRD_SIZE = 7 # size from center to its base (or to the "head")
BIRD_WIDTH = 3

STEP_SIZE = 3 # pixels to move every tick

RANDOM_ROTATE = 5 # angle left/right to rotate every tick
RANDOM_ROTATE_CHANGE = 5 # 1:N chance that it rotates to random direction

BIRD_INTERACTION_DISTANCE = 50 # bird's sight (red border around with toggle - key 4)

ALIGN_DELTA_ANGLE = 15 # angles rotated to align with neighbors

pygame.font.init()
BIRD_DEBUG_FONT = pygame.font.SysFont('Arial', 13)
