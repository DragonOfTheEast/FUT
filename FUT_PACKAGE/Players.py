central = ["ST", "CF", "CAM", "CM", "CDM"]
left_flank = ["LF", "LW", "LM"]
right_flank = ["RF", "RW", "RM"]
positions = {}


class Player:
    def __init__(self, pos, playing_pos, nation,league,team):
        self.playing_pos = playing_pos
        self.pos = pos
        self.nation = nation
        self.league = league
        self.club = team
        self.links = [] ##(player, link value)
        self.chem = None
    def calculate_chem(self):
        pass

    def __str__(self):
        return " ".join([self.pos, self.playing_pos, self.nation, self.league, self.team])

