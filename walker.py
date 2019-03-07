import random
class Walker:
	def __init__(self, cell, seed):
		self.x = cell.x
		self.y = cell.y
		self.id = seed*self.x+self.y
		self.currentcell = cell
	def __hash__(self):
		return hash(self.id)

	def walk(self, arrayofcells):
		choices = []
		if ((self.y-1) > 0 and not arrayofcells[self.y - 1][self.x].explored):
			choices.append(arrayofcells[self.y - 1][self.x])
		if ((self.y+1) < len(arrayofcells) and not arrayofcells[self.y + 1][self.x].explored):
			choices.append(arrayofcells[self.y + 1][self.x])
		if ((self.x-1) > 0 and not arrayofcells[self.y][self.x - 1].explored):
			choices.append(arrayofcells[self.y][self.x - 1])
		if ((self.x+1) < len(arrayofcells[0]) and not arrayofcells[self.y][self.x + 1].explored):
			choices.append(arrayofcells[self.y][self.x + 1])
		if choices:
			return random.choice(choices)
		else:
			return False

	def arrive(self, tuple):
		self.x = tuple[0]
		self.y = tuple[1]
		self.currentcell = tuple[2]
