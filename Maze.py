from enum import Enum
import os
import time
import random
import platform
import curses
chars = ['█','╗','╚','═','║','╔','╝','▓']
#             1   2   1   2   3   1
#             5   3   3   5   5   2
#sum          6   5   4   7   8   3
from cell import Cell
from walker import Walker
sizex, sizey = os.get_terminal_size(1)
if platform.system() == "Windows":
	os.system('mode con: cols=%d lines=%d'%(sizex,sizey))#fix for weird behaivior in win cmd
#utils
def wait(seconds):
	time.sleep(seconds)

if platform.system() == "Windows":
	def clearScreen():
		os.system('cls')
else:
	def clearScreen():
		os.system('clear')
# parts ={
	# "SOLID":'█',
	# "PASSABLE":'░',
	# "ENTITY":'#',
	# "UNEXPLORED":'▓'
	# }
# cellsize = 3

def drawframe(arrayofcells):
	#framestring = ""
	clearScreen()
	for row in arrayofcells:
		framestring = ""
		for col in row:
			framestring += col.repr
		print(framestring, end="", flush=True)


def main(stdscr):
	print("hi")
	#Create cells
	arrayofcells = []
	for row in range(sizey-1):
		arrayofcells.append([])
		for col in range(sizex-1):
			arrayofcells[row].append(Cell(col, row))
	print(sizex, sizey)
	print((sizex-1)*(sizey-1), " cells created")
	#Create walkers
	arrayofwalkers = [Walker(arrayofcells[6][6], 88)]
	#multiple walkers don't really work correctly
	#create stacks
	stacks = {}
	for walker in arrayofwalkers:
		stacks[walker] = []
	print(len(arrayofwalkers), "Walkers ready")
	wait(2)
	stdscr.clear()
	stdscr.refresh()
	#"Game"loop
	explore = True
	drawframe(arrayofcells)
	while explore:
		wait(0.01)
		for walker in arrayofwalkers:
			nextcell = walker.walk(arrayofcells)
			if nextcell:
				stacks[walker].append(nextcell)
				#arrayofcells[walker.y][walker.x].leave(nextcell)
				walker.currentcell.leave(nextcell,stdscr)
				walker.arrive(nextcell.visit(walker))
			else:
				if len(stacks[walker]) > 0:
					nextcell = stacks[walker].pop()
					walker.currentcell.leave(nextcell,stdscr)
					walker.arrive(nextcell.visit(walker))
				else:
					explore = False
		stdscr.refresh()
		#drawframe(arrayofcells)



if __name__ == "__main__":
    curses.wrapper(main)
