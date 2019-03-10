import os
import time
import random
import platform
import curses
from cell import Cell
from walker import Walker
from world import World
sizex, sizey = os.get_terminal_size(1)
if platform.system() == "Windows":
    #  fix for weird behaivior in win cmd
    os.system('mode con: cols=%d lines=%d'%(sizex, sizey))
    #  utils


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
    #  framestring = ""
    clearScreen()
    for row in arrayofcells:
        framestring = ""
        for col in row:
            framestring += col.repr
        print(framestring, end="", flush=True)


def main(stdscr):
    print("hi")
    #  Create cells
    # arrayofcells = []
    # for row in range(sizey-1):
        # arrayofcells.append([])
        # for col in range(sizex-1):
            # arrayofcells[row].append(Cell(col, row))
    gameworld = World(sizex, sizey, stdscr)
    print(sizex, sizey)
    print((sizex-1)*(sizey-1), " cells created")
    #  Create walkers
    arrayofwalkers = [Walker(gameworld.cells[6][6], 88)]
    #  multiple walkers don't really work correctly
    #  create stacks
    stacks = {}
    for walker in arrayofwalkers:
        stacks[walker] = []
    print(len(arrayofwalkers), "Walkers ready")
    wait(2)
    stdscr.clear()
    stdscr.refresh()
    #  "Game"loop
    explore = True
    #  drawframe(gameworld.cells)
    while explore:
        wait(1/60)
        for walker in arrayofwalkers:
            nextcell = walker.walk()
            if nextcell:
                stacks[walker].append(nextcell)
                #  arrayofcells[walker.y][walker.x].leave(nextcell)
                walker.currentcell.leave(nextcell)
                walker.arrive(nextcell.visit(walker))
            else:
                if len(stacks[walker]) > 0:
                    nextcell = stacks[walker].pop()
                    walker.currentcell.leave(nextcell)
                    walker.arrive(nextcell.visit(walker))
                else:
                    explore = False
        stdscr.refresh()
        #  drawframe(arrayofcells)


if __name__ == "__main__":
    curses.wrapper(main)
