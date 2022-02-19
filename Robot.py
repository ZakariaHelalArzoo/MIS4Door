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
        for i, j in View.traversal (3):
            # get color of robot at position x+i, y+j
            v = 0
            
            if v:
                view.add(i,j, v) 
        
        return view

    def compute(self, view):
        x = self.coordinate.getX()
        y = self.coordinate.getY()
        newcolor = self.color

        v = view.categorize ()

        # TODO: calculate coordinate according to view
        if v == 'D':
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
            return None
        return Coordinate(x,y), newcolor

    def move(self, coordinate, color):
        self.coordinate.setX(coordinate.getX())
        self.coordinate.setY(coordinate.getY())
        self.color = color