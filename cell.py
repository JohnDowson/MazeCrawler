chars = ['█','╗','╚','═','║','╔','╝','▓']
#             1   2   1   2   3   1
#             5   3   3   5   5   2
#sum          6   5   4   7   8   3
class Cell:
    connections = [] # for future use instead of path

    def __init__(self, xcoord, ycoord, parent):
        self.repr = chars[0]
        self.path = 0
        self.explored = False
        self.occupied = False
        self.x = xcoord
        self.y = ycoord
        self.parent = parent
        self.neighbours =[]

    def getNeighbours(self): #  parent is a world cell exists in
        if self.x+1 < self.parent.sizex: # neighbour one down
            self.neighbours.append(self.parent.cells[self.y][self.x+1])
        if self.x-1 > 0: # one up
            self.neighbours.append(self.parent.cells[self.y][self.x-1])
        if self.y+1 < self.parent.sizey: # one left
            self.neighbours.append(self.parent.cells[self.y+1][self.x])
        if self.y-1 > 0: # one right
            self.neighbours.append(self.parent.cells[self.y-1][self.x])


    def visit(self, walker):
        self.occupied = True
        if walker.x < self.x:
            self.path = 1
        elif walker.y < self.y:
            self.path = 2
        elif walker.x > self.x:
            self.path = 3
        else:
            self.path = 5
        self.showRepr()
        return self

    def leave(self, nextcell):
        self.occupied = False
        if nextcell.x < self.x:
            self.path += 1
        elif nextcell.y < self.y:
            self.path += 2
        elif nextcell.x > self.x:
            self.path += 3
        else:
            self.path += 5
        if self.explored == False:
            self.explored = True
            if self.path == 3:
                self.repr = chars[6]
            elif self.path == 4:
                self.repr = chars[3]
            elif self.path == 5:
                self.repr = chars[2]
            elif self.path == 6:
                self.repr = chars[1]
            elif self.path == 7:
                self.repr = chars[4]
            elif self.path == 8:
                self.repr = chars[5]
            self.showRepr()

    def showRepr(self):
        if not self.occupied:
            self.parent.surface.addstr(self.y, self.x, self.repr)
        else:
            self.parent.surface.addstr(self.y, self.x, "@")
