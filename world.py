from cell import Cell
from walker import Walker

class World:
    cells = []
    walkers = []

    def __init__(self, sizex, sizey, surface):
        self.surface = surface
        self.sizex = sizex
        self.sizey = sizey
        self.makeCells()

    def makeCells(self):
        for row in range(self.sizey):
            self.cells.append([])
            for col in range(self.sizex):
                self.cells[row].append(Cell(col, row, self))
        for each in self.cells:
            for cell in each:
                cell.getNeighbours()
