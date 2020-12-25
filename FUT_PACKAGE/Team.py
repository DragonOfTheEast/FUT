import FUT_PACKAGE.Players

class Team:
    def __init__(self, formation):
        self.formation = formation
        self.line_up = {}

    #arr is a list of pairs(1st -> Player, 2nd -> Position)
    def build_team(self, arr):
        for i in arr:
            i[]
            self.line_up[i[1]] = i[0]
