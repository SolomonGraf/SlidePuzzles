import random

def isAdjacent(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2) == 1

class Model:
    def __init__(self,size):
        if size > 5 or size < 3:
            raise ValueError("Size must be between 3 and 5")
        self.size = size
        self.grid = [[0 for i in range(size)] for j in range(size)]
        self.currentX = size - 1
        self.currentY = size - 1

    def _inRange(self,x,y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size
    
    def _isEmpty(self,x,y):
        return x == self.currentX and y == self.currentY

    def value(self, x:int, y:int):
        return self.grid[y][x]
    
    def swap(self, x1:int, y1:int, x2:int, y2:int) -> bool:
        if not isAdjacent(x1,y1,x2,y2):
            raise RuntimeError(f"Positions ({x1},{y1}) and ({x2},{y2}) are not adjacent")
        else:
            self.grid[y1][x1], self.grid[y2][x2] = self.grid[y2][x2], self.grid[y1][x1]
        
    def generate(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = self.size*i + j + 1
        self.grid[self.currentY][self.currentX] = -1

    def emptyNeighbors(self):
        emptyNeighbors = [(self.currentX - 1, self.currentY),
                          (self.currentX + 1, self.currentY),
                          (self.currentX, self.currentY - 1),
                          (self.currentX, self.currentY + 1)]
        return list(filter(lambda i : self._inRange(i[0],i[1]),emptyNeighbors))
    
    def shuffle(self):
        for _ in range(200):
            selection = random.choice(self.emptyNeighbors())
            self.swap(selection[0],selection[1],self.currentX,self.currentY)
            self.currentX = selection[0]
            self.currentY = selection[1]
            if self.value(self.currentX,self.currentY) != -1:
                raise RuntimeError(f"Swap error @ {str(selection)} \n" + str(self.grid) + "\n" + str(self.emptyNeighbors()))

    def __str__(self):
        return str(self.grid)