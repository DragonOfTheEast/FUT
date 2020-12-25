central = ["ST", "CF", "CAM", "CM", "CDM"]
left_flank = ["LF", "LW", "LM"]
right_flank = ["RF", "RW", "RM"]
positions = {}


class Player:
    def __init__(self,pos, nation,league,team):
        self.pos = pos
        self.nation = nation
        self.league = league
        self.team = team
        self.links = {}

    def calculate_chem(self, links):
        pass

    def __str__(self):
        return " ".join([self.name, self.pos, self.nation, self.league, self.team])

