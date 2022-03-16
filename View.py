class View:
    robots = []
    doors = []
    rightBoundary = -1
    bottomBoundary = -1
    def __init__(self, robot):
        self.neigh = {}
        self.robot = robot

    def checkAndAdd (self, x, y):
        for robot in View.robots:
            if robot.coordinate.isEqual(x,y):
                self.neigh[x,y] = robot.color

    @staticmethod
    def isInBoundary (x, y):
        if x >= 0 and x < View.rightBoundary and y >=0 and y < View.bottomBoundary:
            return True
        return False
    
    @staticmethod
    def traversal(n):
        for x in range (-n, n+1):
            for y in range (-n, n+1):
                if abs(x)+abs(y) <= n and x != 0 and y != 0:
                    yield x,y

    def categorize(self):
        # TODO: define a function to rotate robots perspective and normalize such that it appears robot is from door1.
        # TODO: view comparison functions

        x = self.robot.coordinate.getX()
        y = self.robot.coordinate.getY()

        door = self.robot.door

        x1,y1,neigh1 = self.setViewToDoorOne(x,y,door)

        if View.isDoor(x, y, self.robot.door): # not complete
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

    def setViewToDoorOne(self, x0, y0, door):
        print("setview")
        nDoorCor = {}
        if door == 1:
            for key, item in self.neigh.items():
                x,y = key
                color = item
                nDoorCor[x, y] = color
            return x0,y0,nDoorCor
        if door == 2:
            for key, item in self.neigh.items():
                x,y = key
                color = item
                nDoorCor[View.rightBoundary-x-1, y] = color
            self.neigh = nDoorCor
            return View.rightBoundary-x0-1,y0,nDoorCor
        if door == 3:
            for key, item in self.neigh.items():
                x,y = key
                color = item
                nDoorCor[x,View.bottomBoundary-y-1] = color
            return x0,View.bottomBoundary-y0-1,nDoorCor
        if door == 4:
            for key, item in self.neigh.items():
                x,y = key
                color = item
                nDoorCor[View.rightBoundary-x-1, View.bottomBoundary-y-1] = color
            return View.rightBoundary-x0-1, View.bottomBoundary-y0-1,nDoorCor

