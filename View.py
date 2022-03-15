class View:
    robots = []
    doors = []
    rightBoundary = -1
    bottomBoundary = -1
    def __init__(self):
        self.neigh = {}

    def checkAndAdd (self, x, y):
        for robot in View.robots:
            if robot.coordinate.isEqual(x,y):
                self.neigh[x,y] = robot.color

    def isInBoundary (self, x, y):
        if x >= 0 and x < View.rightBoundary and y >=0 and y < View.bottomBoundary:
            return True
        return False
    
    @staticmethod
    def traversal(n):
        for x in range (-n, n+1):
            for y in range (-n, n+1):
                if abs(x)+abs(y) <= n and x != 0 and y != 0:
                    yield x,y

    def categorize(self, x, y, door, direction):
        # TODO: define a function to rotate robots perspective and normalize such that it appears robot is from door1.
        # TODO: view comparison functions

        if View.isDoor(x, y, door): # not complete
            return 'D'

        return

    @staticmethod
    def getPosCol(x,y):
        for robot in View.robots:
            if (robot.coordinate.isEqual(x,y)):
                return robot.color
        return -1

    @staticmethod
    def isDoor(x, y, doorNo):
        print(doorNo)
        if(View.doors[doorNo-1].coordinate.isEqual(x,y)):
            return True
        return False
