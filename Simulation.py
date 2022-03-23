from Coordinate import Coordinate
from Door import Door
from View import View
import Grid


class Simulate:

    def __init__(self, numOfRows, numOfCols):
        self.robots = []
        self.doors = []
        self.numOfRows = numOfRows
        self.numOfCols = numOfCols
        self.Door1 = Door(Coordinate(numOfRows, numOfCols), 1)  # bottom-right
        self.Door2 = Door(Coordinate(-1, numOfCols), 2)  # bottom-left
        self.Door3 = Door(Coordinate(numOfRows, -1), 3)  # top-right
        self.Door4 = Door(Coordinate(-1, -1), 4)  # top-left
        self.doors.append(self.Door1)
        self.doors.append(self.Door2)
        self.doors.append(self.Door3)
        self.doors.append(self.Door4)
        View.doors = self.doors
        View.bottomBoundary = numOfRows
        View.rightBoundary = numOfCols

    def executeCycle(self):
        Grid.render(self.robots, self.doors, self.numOfRows, self.numOfCols)

        # print (self.robots)

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

            # TODO: check using active robots
            if r1 or r2 or r3 or r4:
                isFinished = False

            nextState = {}

            for robot in self.robots:
                if robot.color == 3 or robot == r1 or robot == r2 or robot == r3 or robot == r4:
                    continue
                view = robot.look()
                color, coordinate = robot.compute(view)
                if coordinate:
                    nextState[robot] = color, coordinate

            for key, value in nextState.items():
                color, coordinate = value
                key.move(coordinate, color)
                isFinished = False

            print("look compute done")
            # print(self.robots)
            Grid.render(self.robots, self.doors, self.numOfRows, self.numOfCols)


if __name__ == "__main__":
    numOfRows = 11
    numOfCols = 11
    obj = Simulate(numOfRows, numOfCols)
    obj.executeCycle()
