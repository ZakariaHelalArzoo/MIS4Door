import random
import math
from collections import defaultdict

from Coordinate import Coordinate
from Robot import Robot
from Door import Door
import Grid
class Simulate:

    def __init__(self, n, m):
        self.robots = []
        self.n = n
        self.m = m
        self.Door1 = Door(Coordinate(m, n), 1) # bottom-right
        self.Door2 = Door(Coordinate(0, n), 2) # bottom-left
        self.Door3 = Door(Coordinate(m, 0), 3) # top-right
        self.Door4 = Door(Coordinate(0, 0), 4) # top-left

    def executeCycle(self):        
        Grid.render(self.robots)

        print (self.robots)

        isFinished = False

        id = 0

        while not isFinished:
            isFinished = True
            r1 = self.Door1.placeRobot(id)
            if r1:
                id = id + 1
                self.robots.append(r1)
            r2 = self.Door2.placeRobot(id)
            if r2:
                id = id + 1
                self.robots.append(r2)
            r3 = self.Door3.placeRobot(id)
            if r3:
                id = id + 1
                self.robots.append(r3)
            r4 = self.Door4.placeRobot(id)
            if r4:
                id = id + 1
                self.robots.append(r4)
            
            if r1 or r2 or r3 or r4:
                isFinished = False

            for robot in self.robots:
                if (robot.color == 'F'):
                    continue
                view = robot.look()
                coordinate = robot.compute(view)
                if coordinate:
                    robot.move(coordinate)
                    isFinished = False
                
            print("look compute done")
            print (self.robots)
            Grid.render(self.robots)

if __name__ == "__main__":

    for i in range(10):
        obj = Simulate(i,i)
        obj.executeCycle()
        print("Finished ", i)
    while True:
        continue
