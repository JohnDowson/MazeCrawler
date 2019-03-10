import random
class Walker:
    def __init__(self, cell, seed):
        self.x = cell.x
        self.y = cell.y
        self.id = seed*self.x+self.y
        self.currentcell = cell
    def __hash__(self):
        return hash(self.id)

    def walk(self):
        choices = []
        for choice in self.currentcell.neighbours:
            if not choice.explored:
                choices.append(choice)
        if choices:
            return random.choice(choices)
        else:
            return False

    def arrive(self, cell):
        self.x = cell.x
        self.y = cell.y
        self.currentcell = cell
