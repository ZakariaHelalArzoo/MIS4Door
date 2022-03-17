from Coordinate import Coordinate
from View import View
import enum
VISIBILITY_RADIUS = 3
class Direction(enum.Enum):
    N=[0,-1]
    S=[0,1]
    W=[-1,0]
    E=[1,0]
class Robot:
    def __init__(self, id, coordinate, color, door) -> None:
        self.id = id
        self.coordinate = coordinate
        self.color = color
        self.door = door
        if door == 1 or door == 2:
            self.direction = Direction.N
        else:
            self.direction = Direction.S

    def __repr__ (self):
        return f"Robot: {self.id} {self.coordinate} color:{self.color} door:{self.door} direction:{self.direction}"

    def look(self):

        x = self.coordinate.getX()
        y = self.coordinate.getY()

        view = View(self)

        for i, j in View.traversal (3):
            if View.isInBoundary(x+i, y+j):
                view.checkAndAdd(x+i, y+j)
        
        return view

    def compute(self, view):
        x = self.coordinate.getX()
        y = self.coordinate.getY()
        color = self.color
        door = self.door

        v = view.categorize ()
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
            if door == 1:
                p1 = self.getCorToPort(x-1, y)
                p2 = self.getCorToPort(x,y-1)

                if p1>p2:
                    x = x-1
                    self.direction = Direction.W
                else:
                    y = y-1
                    self.direction = Direction.N
            elif door == 2:
                p1 = self.getCorToPort(x+1,y)
                p2 = self.getCorToPort(x,y-1)
                if p1>p2:
                    x = x+1
                    self.direction = Direction.W
                else:
                    y = y-1
                    self.direction = Direction.N
            elif door == 3:
                p1 = self.getCorToPort(x-1,y)
                p2 = self.getCorToPort(x,y+1)
                if p1>p2:
                    x = x-1
                    self.direction = Direction.W
                else:
                    y = y+1
                    self.direction = Direction.S
            elif door == 4:
                p1 = self.getCorToPort(x+1,y)
                p2 = self.getCorToPort(x,y+1)
                if p1>p2:
                    x = x+1
                    self.direction = Direction.W
                else:
                    y = y+1
                    self.direction = Direction.S
        elif v == 'M':
            x += self.direction[0]
            y += self.direction[1]
        elif v == 'C':
            if door == 1:
                self.direction = Direction.W
            if door == 2:
                self.direction = Direction.E
            if door == 3:
                self.direction = Direction.W
            if door == 4:
                self.direction = Direction.E
            x += self.direction[0]
            y += self.direction[1]
        elif v == 'F':
            color = 3
        elif v == 'Col1':
            if door == 3:
                self.direction = Direction.W
                x += self.direction[0]
                y += self.direction[1]
            if door == 4:
                self.direction = Direction.E
                x += self.direction[0]
                y += self.direction[1]
        elif v == 'Col2':
            if door == 3 or door == 4:
                x += self.direction[0]
                y += self.direction[1]
        elif v == 'Col3':
            if door == 1:
                self.direction = Direction.W
                x += self.direction[0]
                y += self.direction[1]
            if door == 2:
                self.direction = Direction.E
                x += self.direction[0]
                y += self.direction[1]
        elif v == 'Col4':
            if door == 3 or door == 4:
                color = 3
            pass
        elif v == 'Col5':
            if door == 3:
                self.direction = Direction.W
                x += self.direction[0]
                y += self.direction[1]
            if door == 4:
                self.direction = Direction.E
                x += self.direction[0]
                y += self.direction[1]
        elif v == 'Col6':
            if door == 1 or door == 2:
                color = 3
        elif v == 'Colf1':
            color = 3
        elif v == 'Colf2':
            if door == 2 or door == 4:
                if self.direction == Direction.N:
                    x += Direction.S[0]
                    y += Direction.S[1]
                elif self.direction == Direction.S:
                    x += Direction.N[0]
                    y += Direction.N[1]
                elif self.direction == Direction.W:
                    x += Direction.E[0]
                    y += Direction.E[1]
                elif self.direction == Direction.E:
                    x += Direction.W[0]
                    y += Direction.W[1]
            else:
                x += self.direction[0]
                y += self.direction[1]
            color = 3
        elif v == 'Colf3':
            if door == 1 or door == 3:
                if self.direction == Direction.N:
                    x += Direction.S[0]
                    y += Direction.S[1]
                elif self.direction == Direction.S:
                    x += Direction.N[0]
                    y += Direction.N[1]
                elif self.direction == Direction.W:
                    x += Direction.E[0]
                    y += Direction.E[1]
                elif self.direction == Direction.E:
                    x += Direction.W[0]
                    y += Direction.W[1]
            else:
                x += self.direction[0]
                y += self.direction[1]
            color = 3
        elif v == 'Colf4':
            color = 3
        elif v == 'Colf5':
            if door == 1 or door == 3:
                x += self.direction[0]
                y += self.direction[1]
            color = 3
        elif v == 'Colf6':
            if door == 1 or door == 3:
                x += self.direction[0]
                y += self.direction[1]
            color = 3
        elif v == 'Colf7':
            if door == 2 or door == 4:
                x += self.direction[0]
                y += self.direction[1]
            color = 3
        elif v == 'Colf8':
            if door == 2 or door == 4:
                if self.direction == Direction.N:
                    x += Direction.S[0]
                    y += Direction.S[1]
                elif self.direction == Direction.S:
                    x += Direction.N[0]
                    y += Direction.N[1]
                elif self.direction == Direction.W:
                    x += Direction.E[0]
                    y += Direction.E[1]
                elif self.direction == Direction.E:
                    x += Direction.W[0]
                    y += Direction.W[1]
            else:
                x += self.direction[0]
                y += self.direction[1]
            color = 3
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

    @staticmethod
    def getCorToPort(x,y):
        if View.isInBoundary(x,y):
            return (View.bottomBoundary-y-1)*View.rightBoundary + View.rightBoundary-x
        return -1
