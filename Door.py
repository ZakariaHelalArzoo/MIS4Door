from Coordinate import Coordinate
from View import View
from Robot import Robot
class Door:
    def __init__(self, coordinate, no):
        self.currColor = 0
        self.no = no
        self.coordinate = coordinate

    def placeRobot(self, id):
        view = View()
        if False: # TODO: check if door is empty
            return
        for i, j in View.traversal (3):
            if False: #TODO: check if positions around door are empty
                return
        robot = Robot(id, Coordinate(self.coordinate.getX(), self.coordinate.getY()), self.currColor, self.no)
        self.currColor = (self.currColor + 1) % 3
        return robot
        
        