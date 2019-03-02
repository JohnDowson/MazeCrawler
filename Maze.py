import os
import time
import random
import platform
#from enum import Enum
os.system('mode con: cols=80 lines=40')
sizex, sizey = os.get_terminal_size(1)
# sizex, sizey = 80, 40
#utils
def wait(seconds):
	time.sleep(seconds)
def clearScreen():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')

chars = ['█','╗','╚','═','║','╔','╝','▓']
#             1   2   1   2   3   1
#             5   3   3   5   5   2
#sum          6   5   4   7   8   3
class Cell:
	def __init__(self, xcoord, ycoord):
		self.x = xcoord
		self.y = ycoord
		self.explored = False
		self.repr = chars[0]
		self.path = 0

	def visit(self, walker):
		self.repr = chars[5]
		if walker.x < self.x:
			self.path = 1
		elif walker.y < self.y:
			self.path = 2
		elif walker.x > self.x:
			self.path = 3
		else:
			self.path = 5
		return (self.x, self.y)

	def leave(self, nextcell):
		if nextcell.x < self.x:
			self.path += 1
		elif nextcell.y < self.y:
			self.path += 2
		elif nextcell.x > self.x:
			self.path += 3
		else:
			self.path += 5
		
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
		
		self.explored = True
			
class Walker:
	def __init__(self, cell, seed):
		self.x = cell.x
		self.y = cell.y
		self.id = seed*self.x+self.y
	def __hash__(self):
		return hash(self.id)
		
	def walk(self, arrayofcells):
		choices = []
		if (self.y > 0 and not arrayofcells[self.y - 1][self.x].explored):
			choices.append(arrayofcells[self.y - 1][self.x])
		if ((self.y-1) < len(arrayofcells) and not arrayofcells[self.y + 1][self.x].explored):
			choices.append(arrayofcells[self.y + 1][self.x])
		if ((self.x-1) > 0 and not arrayofcells[self.y][self.x - 1].explored):
			choices.append(arrayofcells[self.y][self.x - 1])
		if (self.x < len(arrayofcells[0]) and not arrayofcells[self.y][self.x + 1].explored):
			choices.append(arrayofcells[self.y][self.x + 1])
		if choices:
			return random.choice(choices)
		else:
			return False

	def arrive(self, tuple):
		self.x = tuple[0]
		self.y = tuple[1]



def main():
	print("hi")
	#Create cells
	arrayofcells = []
	for row in range(sizey):
		arrayofcells.append([])
		for col in range(sizex):
			arrayofcells[row].append(Cell(col, row))
	print(sizex, sizey)
	print(sizex*sizey, " cells created")
	#Create walkers
	arrayofwalkers = [Walker(arrayofcells[6][6], 88)]
	#arrayofwalkers.append(Walker(arrayofcells[10][10], 99))
	#create stacks
	stacks = {}
	for walker in arrayofwalkers:
		stacks[walker] = []
	print(len(arrayofwalkers), "Walkers ready")
	wait(2)
	clearScreen()
	#"Game"loop
	while True:
		wait(0.01)
		framestring = ""
		clearScreen()
		for walker in arrayofwalkers:
			nextcell = walker.walk(arrayofcells)
			if nextcell:
				stacks[walker].append(nextcell)
				arrayofcells[walker.y][walker.x].leave(nextcell)
				walker.arrive(nextcell.visit(walker))
			else:
				nextcell = stacks[walker].pop()
				walker.arrive(nextcell.visit(walker))
		for row in arrayofcells:
			for col in row:
				framestring += col.repr
		print(framestring, end="")


	
if __name__ == "__main__":
    main()