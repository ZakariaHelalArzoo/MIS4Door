class View:
    def __init__(self):
        self.d = {}

    def add (self, x, y, color):
        self.d[x,y] = color
    
    @staticmethod
    def traversal(n):
        for x in range (-n, n+1):
            for y in range (-n, n+1):
                if abs(x)+abs(y) <= n and x != 0 and y != 0:
                    yield x,y

    def categorize(self):
        return