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
BLOCK_SIZE = 40  # Set the size of the grid block
TOP_MARGIN = 60
LEFT_MARGIN = 60
DOOR_SPACING = BLOCK_SIZE
pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def render(robots, doors, numberOfRows, numberOfCols):
    WINDOW.fill(BLACK)
    drawDoors(doors)
    drawGrid(numberOfRows, numberOfCols)
    renderRobots(robots)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    time.sleep(0.5)
    pygame.display.update()


def drawGrid(numberOfRows, numberOfCols):
    for x in range(0, (numberOfRows - 1) * BLOCK_SIZE, BLOCK_SIZE):
        for y in range(0, (numberOfCols - 1) * BLOCK_SIZE, BLOCK_SIZE):
            rect = pygame.Rect(x + LEFT_MARGIN + DOOR_SPACING / 2, y + TOP_MARGIN + DOOR_SPACING / 2, BLOCK_SIZE,
                               BLOCK_SIZE)
            pygame.draw.rect(WINDOW, WHITE, rect, 1)


def drawDoors(doors):
    # bottom-right
    rect = pygame.Rect(doors[0].coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN,
                       doors[0].coordinate.getY() * BLOCK_SIZE + TOP_MARGIN, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(WINDOW, WHITE, rect, 1)

    # bottom-left
    rect = pygame.Rect(doors[1].coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN,
                       doors[1].coordinate.getY() * BLOCK_SIZE + TOP_MARGIN, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(WINDOW, WHITE, rect, 1)

    # top-right
    rect = pygame.Rect(doors[2].coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN,
                       doors[2].coordinate.getY() * BLOCK_SIZE + TOP_MARGIN, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(WINDOW, WHITE, rect, 1)

    # top-left
    rect = pygame.Rect(doors[3].coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN,
                       doors[3].coordinate.getY() * BLOCK_SIZE + TOP_MARGIN, BLOCK_SIZE, BLOCK_SIZE)
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

    inDoorNo = robot.inDoor()
    if inDoorNo == 1:  # robot is inside door
        pygame.draw.circle(WINDOW, color, (robot.coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN + DOOR_SPACING / 2,
                                           robot.coordinate.getY() * BLOCK_SIZE + TOP_MARGIN + DOOR_SPACING / 2),
                           ROBOT_RADIUS)
        return
    if inDoorNo == 2:  # robot is inside door
        pygame.draw.circle(WINDOW, color, (robot.coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN + DOOR_SPACING / 2,
                                           robot.coordinate.getY() * BLOCK_SIZE + TOP_MARGIN + DOOR_SPACING / 2),
                           ROBOT_RADIUS)
        return
    if inDoorNo == 3:  # robot is inside door
        pygame.draw.circle(WINDOW, color, (robot.coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN + DOOR_SPACING / 2,
                                           robot.coordinate.getY() * BLOCK_SIZE + TOP_MARGIN + DOOR_SPACING / 2),
                           ROBOT_RADIUS)
        return
    if inDoorNo == 4:  # robot is inside door
        pygame.draw.circle(WINDOW, color, (robot.coordinate.getX() * BLOCK_SIZE + LEFT_MARGIN + DOOR_SPACING / 2,
                                           robot.coordinate.getY() * BLOCK_SIZE + TOP_MARGIN + DOOR_SPACING / 2),
                           ROBOT_RADIUS)
        return

    pygame.draw.circle(WINDOW, color, (robot.coordinate.getX() * BLOCK_SIZE + DOOR_SPACING / 2 + LEFT_MARGIN,
                                       robot.coordinate.getY() * BLOCK_SIZE + DOOR_SPACING / 2 + TOP_MARGIN),
                       ROBOT_RADIUS)
