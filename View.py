class View:
    robots = []
    doors = []
    rightBoundary = -1
    bottomBoundary = -1
    finalColor = 3

    def __init__(self, robot):
        self.neigh = {}
        self.robot = robot

    def __repr__(self):
        return f"View: {self.robots} {self.doors} neigh: {self.neigh} robot: {self.robot}"

    def checkAndAdd(self, x, y):
        for robot in View.robots:
            if robot.coordinate.isEqual(x, y):
                self.neigh[x, y] = robot.color

    @staticmethod
    def isInBoundary(x, y):
        if 0 <= x < View.rightBoundary and 0 <= y < View.bottomBoundary:
            return True
        return False

    @staticmethod
    def traversal(n):
        for x in range(-n, n + 1):
            for y in range(-n, n + 1):
                if x == 0 and y == 0:
                    continue
                if abs(x) + abs(y) <= n:
                    yield x, y

    def categorize(self):
        # TODO: define a function to rotate robots perspective and normalize such that it appears robot is from door1.
        # TODO: view comparison functions

        x = self.robot.coordinate.getX()
        y = self.robot.coordinate.getY()

        door = self.robot.door
        robotColor = self.robot.color

        x1, y1, neigh1 = self.setViewToDoorOne(x, y, door)
        # View D
        if view := self.viewD(x, y, self.neigh):
            return view
        

        #View DC
        # elif view := self.viewDC(x, y, neigh1):
        #     return view

        # View F
        elif view := self.viewF(x1, y1, neigh1):
            return view 

        # View Col2
        elif view := self.viewCol2(x1, y1, neigh1, robotColor):
            return view

        # View Col4
        elif view := self.viewCol4(x1, y1, neigh1, robotColor):
            return view
        

        # View Col5
        elif view := self.viewCol5(x1, y1, neigh1, robotColor):
            return view

        # View Col1
        elif view := self.viewCol1(x1, y1, neigh1, robotColor):
            return view
        

        # View Col6
        elif view := self.viewCol6(x1, y1, neigh1, robotColor):
            return view

        # View Col3
        elif view := self.viewCol3(x1, y1, neigh1, robotColor):
            return view
        
        # View Colf2
        elif view := self.viewColf2(x1, y1, neigh1, robotColor):
            return view

        # View Colf4
        elif view := self.viewColf4(x1, y1, neigh1):
            return view

        # View Colf1
        elif view := self.viewColf1(x1, y1, neigh1, robotColor):
            return view

        # View Colf3
        elif view := self.viewColf3(x1, y1, neigh1, robotColor):
            return view
    

        # View Colf6
        elif view := self.viewColf6(x1, y1, neigh1, robotColor):
            return view
        

        # View Colf7
        elif view := self.viewColf7(x1, y1, neigh1, robotColor):
            return view

        # View Colf5
        elif view := self.viewColf5(x1, y1, neigh1, robotColor):
            return view
        

        # View Colf8
        elif view := self.viewColf8(x1, y1, neigh1, robotColor):
            return view

        # View C
        elif view := self.viewC(x1, y1, neigh1):
            return view
        

        return 'M'

    
    def viewD(self, x, y, neigh):
        if View.isDoor(x, y, self.robot.door):
            if not self.hasUnfinishedRobot(neigh): 
                if self.robot.door == 1 and ((x -1, y - 1) in neigh or (x-2, y-1) in neigh):
                    return 'I'
                elif self.robot.door == 2 and ((x + 1, y - 1) in neigh or (x+2, y-1) in neigh):
                    return 'I'
                elif self.robot.door == 3 and ((x - 1, y + 1) in neigh or (x-2, y+1) in neigh):
                    return 'I'
                elif self.robot.door == 4 and ((x + 1, y + 1) in neigh or (x+2, y+1) in neigh):
                    return 'I'

                return 'D'
            else:
                return 'I'
        
        return False

    def viewDC(self, x1, y1, neigh1):
        if x1 == View.rightBoundary - 1 and y1 == View.bottomBoundary - 1:
            if (x1-1, y1) not in neigh1 or not (x1, y1-1) in neigh1:
                return 'DC'
            
            return 'I'
        
        return False

    def viewC(self, x1, y1, neigh1):
        if ((x1, y1 - 1) in neigh1 or (x1 - 1, y1 - 1) in neigh1) and (x1 == self.rightBoundary-1 and (neigh1.get((x1, y1 - 1)) == View.finalColor or neigh1.get((x1 - 1, y1 - 1)) == View.finalColor)):
            return 'C'
            
        return False


    def viewF(self, x1, y1, neigh1):
        if (x1 - 1, y1 - 1) in neigh1 and (x1, y1 - 2) in neigh1 and (x1 - 2, y1) in neigh1 and (
                x1 - 2, y1 - 2) in neigh1 and x1 == self.rightBoundary-1 and x1 == self.rightBoundary - 1 and neigh1.get((x1 - 1, y1 - 1)) == View.finalColor and neigh1.get(
                (x1, y1 - 2)) == View.finalColor and neigh1.get((x1 - 2, y1)) == View.finalColor and neigh1.get(
                (x1 - 2, y1 - 2)) == View.finalColor:
            return 'F'

        elif (x1 + 1, y1 - 1) in neigh1 and (x1 - 1, y1 - 1) in neigh1 and (x1 - 2, y1) in neigh1 and neigh1.get((x1 + 1, y1 - 1)) == View.finalColor and neigh1.get(
                    (x1 - 1, y1 - 1)) == View.finalColor and neigh1.get((x1 - 2, y1)) == View.finalColor:
            return 'F'

        elif (x1 - 2, y1) in neigh1 and neigh1.get((x1 - 2, y1)) == View.finalColor:
            return 'F'
            
        return False

    def viewCol1(self, x1, y1, neigh1, robotColor):
        if (x1, y1 - 2) in neigh1 and neigh1.get((x1, y1 - 2)) == robotColor:
            return 'Col1'
            
        return False

    def viewCol2(self, x1, y1, neigh1, robotColor):
        if (x1, y1 - 3) in neigh1 and neigh1.get((x1, y1 - 3)) == robotColor:
            return 'Col2'
            
        return False

    def viewCol3(self, x1, y1, neigh1, robotColor):
        if (x1, y1 - 3) in neigh1 and neigh1.get((x1, y1 - 3)) != robotColor and (self.robot.door == 3 or self.robot.door == 4 or ((x1 - 2, y1 - 1) in neigh1 and neigh1.get((x1 - 2, y1 - 1)) == robotColor)) and (x1, y1-1) not in neigh1 and (x1, y1-2) not in neigh1 and neigh1.get((x1, y1 - 3)) != View.finalColor:
            return 'Col3'
            
        return False
    
    def viewCol4(self, x1, y1, neigh1, robotColor):
        if (x1 - 2, y1) in neigh1 and (x1, y1 - 2) in neigh1 and neigh1.get((x1 - 2, y1)) == View.finalColor and neigh1.get((x1, y1 - 2)) == robotColor:
                return 'Col4'
                
        return False

    def viewCol5(self, x1, y1, neigh1, robotColor):
        if (x1 - 3, y1 ) in neigh1 and (x1, y1 - 2) in neigh1 and neigh1.get((x1 - 3, y1 )) == View.finalColor and neigh1.get((x1, y1 - 2)) == robotColor:
            return 'Col5'
            
        return False

    def viewCol6(self, x1, y1, neigh1, robotColor):
        if (x1 - 2, y1) in neigh1 and (x1, y1 - 3) in neigh1 and neigh1.get((x1 - 2, y1)) == View.finalColor and neigh1.get((x1, y1 - 3)) != robotColor  and neigh1.get((x1, y1 - 3)) != View.finalColor :
                return 'Col6'
                
        return False

    def viewColf1(self, x1, y1, neigh1, robotColor):
        if (x1 - 2, y1) in neigh1 and neigh1.get((x1 - 2, y1)) == robotColor:
                return 'Colf1'
                
        return False
    
    def viewColf2(self, x1, y1, neigh1, robotColor):
        if (x1, y1 - 1) in neigh1 and (x1 - 2, y1 - 1) in neigh1 and (x1 - 2, y1) in neigh1 and neigh1.get((x1, y1 - 1)) == View.finalColor and neigh1.get(
                    (x1 - 2, y1 - 1)) == View.finalColor and neigh1.get((x1 - 2, y1)) == robotColor:
                return 'Colf2'
                
        return False

    def viewColf3(self, x1, y1, neigh1, robotColor):
        if (x1, y1 - 1) in neigh1 and (x1 - 2, y1 - 1) in neigh1 and (x1 - 2, y1) in neigh1 and neigh1.get((x1, y1 - 1)) == View.finalColor and neigh1.get(
                    (x1 - 2, y1 - 1)) == View.finalColor and neigh1.get((x1 - 2, y1)) != robotColor and neigh1.get((x1 - 2, y1)) != View.finalColor:
                return 'Colf3'
                
        return False

    def viewColf4(self, x1, y1, neigh1):
        if (x1 - 1, y1 - 1) in neigh1 and (x1 + 1, y1 - 1) in neigh1 and (x1 - 2, y1) in neigh1 and neigh1.get((x1 - 1, y1 - 1)) == View.finalColor and neigh1.get((x1 + 1, y1 - 1)) == View.finalColor:
                return 'Colf4'

        elif (x1 - 1, y1 - 1) in neigh1 and (x1 - 2, y1) in neigh1 and neigh1.get((x1 - 1, y1 - 1)) == View.finalColor :
                return 'Colf4'
                
        return False

    def viewColf5(self, x1, y1, neigh1, robotColor):
        if (x1 - 3, y1) in neigh1 and neigh1.get((x1 - 3, y1)) == robotColor: # also check if no other robots around
                return 'Colf5'
                
        return False

    def viewColf6(self, x1, y1, neigh1, robotColor):
        if (x1, y1 - 1) in neigh1 and (
                x1 - 3, y1) in neigh1 and neigh1.get((x1, y1 - 1)) == View.finalColor and neigh1.get((x1 - 3, y1)) == robotColor:
                return 'Colf6'
                
        return False

    def viewColf7(self, x1, y1, neigh1, robotColor):
        if (x1 - 1, y1 - 1) in neigh1 and (
                x1 - 3, y1) in neigh1 and neigh1.get(
                    (x1 - 1, y1 - 1)) == View.finalColor and neigh1.get((x1 - 3, y1)) == robotColor:
                return 'Colf7'
                
        return False

    def viewColf8(self, x1, y1, neigh1, robotColor):
        if (x1 + 1, y1 - 1) in neigh1 and (x1 - 1, y1 - 1) in neigh1 and (
                x1 - 3, y1) in neigh1 and neigh1.get((x1 + 1, y1 - 1)) == View.finalColor and neigh1.get(
                    (x1 - 1, y1 - 1)) == View.finalColor and neigh1.get((x1 - 3, y1)) != robotColor and neigh1.get((x1 - 3, y1)) != View.finalColor:
                return 'Colf8'

        elif (self.robot.door == 2 or self.robot.door == 4
                ) and ((x1, y1 - 1) in neigh1 and neigh1.get((x1, y1 - 1)) == View.finalColor
                ) and ((x1 - 2, y1 - 1) in neigh1 and neigh1.get((x1 - 2, y1 - 1)) == View.finalColor
                ) and ((x1 - 3, y1) in neigh1 and neigh1.get((x1 - 3, y1)) != robotColor and neigh1.get((x1 - 3, y1)) != View.finalColor):
            return 'Colf8'
        
        return False

    @staticmethod
    def hasUnfinishedRobot(neigh):
        for key, color in neigh.items():
            if color != View.finalColor:
                return True

        return False

    @staticmethod
    def getPosCol(x, y):
        for robot in View.robots:
            if robot.coordinate.isEqual(x, y):
                return robot.color
        return -1

    @staticmethod
    def isDoor(x, y, doorNo):
        #print(doorNo)
        if View.doors[doorNo - 1].coordinate.isEqual(x, y):
            return True
        return False

    def setViewToDoorOne(self, x0, y0, door):
        #print("setview")
        nDoorCor = {}
        if door == 1:
            for key, item in self.neigh.items():
                x, y = key
                color = item
                nDoorCor[x, y] = color
            return x0, y0, nDoorCor
        elif door == 2:
            for key, item in self.neigh.items():
                x, y = key
                color = item
                nDoorCor[View.rightBoundary - x - 1, y] = color

            return View.rightBoundary - x0 - 1, y0, nDoorCor
        elif door == 3:
            for key, item in self.neigh.items():
                x, y = key
                color = item
                nDoorCor[x, View.bottomBoundary - y - 1] = color
            return x0, View.bottomBoundary - y0 - 1, nDoorCor

        else:
            for key, item in self.neigh.items():
                x, y = key
                color = item
                nDoorCor[View.rightBoundary - x - 1, View.bottomBoundary - y - 1] = color
            return View.rightBoundary - x0 - 1, View.bottomBoundary - y0 - 1, nDoorCor
