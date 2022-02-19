import pygame, pygame.freetype
import sys
import time
from Robot import Robot
from Coordinate import Coordinate

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROBOT_RADIUS = 10
BLOCK_SIZE = 40 #Set the size of the grid block


def render(robots):
    global WINDOW
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    WINDOW.fill(BLACK)

    drawGrid()
    renderRobots(robots)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            sys.exit()
    
    # time.sleep(0)
    pygame.display.update()


def drawGrid():
    
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(WINDOW, WHITE, rect, 1)

def renderRobots(robots):
    for robot in robots:
        renderRobot(robot)

def renderRobot(robot):
    color = WHITE
    if robot.color == 0:
        color = RED
    elif robot.color == 1:
        color = BLUE
    elif robot.color == 2:
        color = GREEN
    pygame.draw.circle(WINDOW, color, (robot.coordinate.getX() * BLOCK_SIZE, robot.coordinate.getY() * BLOCK_SIZE), ROBOT_RADIUS)
