from Coordinate import Coordinate
from View import View
from Robot import Robot
class Door:
    def __init__(self, coordinate, no):
        self.currColor = 0
        self.no = no
        self.coordinate = coordinate
        print(no, coordinate)

    def placeRobot(self, id):
        if View.getPosCol(self.coordinate.getX(), self.coordinate.getY()) >= 0:
            return
        for i, j in View.traversal (3):
            if View.getPosCol(self.coordinate.getX()+i, self.coordinate.getY()+j) >= 0:
                if self.no == 1 and i == -1 and j == -1:
                    continue
                if self.no == 2 and i == 1 and j == -1:
                    continue
                if self.no == 3 and i == -1 and j == 1:
                    continue
                if self.no == 4 and i == 1 and j == 1:
                    continue
                return
        robot = Robot(id, Coordinate(self.coordinate.getX(), self.coordinate.getY()), self.currColor, self.no)
        View.robots.append(robot)
        self.currColor = (self.currColor + 1) % 3
        return robot
        
        