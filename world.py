from cell import Cell
from walker import Walker
class World:
	def __init__(self, sizeTuple, walkersNumber):
		self.cells = []
		self.walkers = []
		for row in range(sizey-1):
			self.cells.append([])
			for col in range(sizex-1):
				self.cells[row].append(Cell(col, row))
		for i in range(walkersNumber):
			self.walkers = [Walker(self.cells[x][y], i)]
