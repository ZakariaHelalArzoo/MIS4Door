from Coordinate import Coordinate
from View import View
import enum
VISIBILITY_RADIUS = 3
class Direction(enum.Enum):
    UP=[0,-1]
    DOWN=[0,1]
    LEFT=[-1,0]
    RIGHT=[1,0]
class Robot:
    def __init__(self, id, coordinate, color, door) -> None:
        self.id = id
        self.coordinate = coordinate
        self.color = color
        self.door = door
        if door == 1 or door == 2:
            self.direction = Direction.UP
        else:
            self.direction = Direction.DOWN

    def __repr__ (self):
        return f"Robot: {self.id} {self.coordinate} color:{self.color} door:{self.door} direction:{self.direction}"

    def look(self):
        view = View()

        x = self.coordinate.getX()
        y = self.coordinate.getY()

        for i, j in View.traversal (3):
            if view.isInBoundary(x+i, y+j):
                view.checkAndAdd(x+i, y+j)
        
        return view

    def compute(self, view):
        x = self.coordinate.getX()
        y = self.coordinate.getY()
        color = self.color
        door = self.door

        v = view.categorize (x, y, door, self.direction)
        print(self, v)

        # TODO: calculate coordinate according to view
        if v == 'D':
            if door == 1:
                x,y = view.rightBoundary-1, view.bottomBoundary-1
            elif door == 2:
                x,y = 0, view.bottomBoundary-1
            elif door == 3:
                x,y = view.rightBoundary-1, 0
            elif door == 4:
                x,y = 0, 0
            pass
        elif v == 'DC':
            pass
        elif v == 'M':
            pass
        elif v == 'C':
            pass
        elif v == 'Col1':
            pass
        elif v == 'Col2':
            pass
        elif v == 'Col3':
            pass
        elif v == 'Col4':
            pass
        elif v == 'Col5':
            pass
        elif v == 'Col6':
            pass
        elif v == 'Colf1':
            pass
        elif v == 'Colf2':
            pass
        elif v == 'Colf3':
            pass
        elif v == 'Colf4':
            pass
        elif v == 'Colf5':
            pass
        elif v == 'Colf6':
            pass
        elif v == 'Colf7':
            pass
        elif v == 'Colf8':
            pass
        else:
            return None, None
        return (color, Coordinate(x,y))

    def move(self, coordinate, color):
        self.coordinate.setX(coordinate.getX())
        self.coordinate.setY(coordinate.getY())
        self.color = color

    def inDoor(self):
        if View.isDoor(self.coordinate.getX(), self.coordinate.getY(), self.door):
            return self.door
        return -1