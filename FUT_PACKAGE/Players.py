central = {"ST", "CF", "CAM", "CM", "CDM"}
left_flank = {"LF", "LW", "LM"}
right_flank = {"RF", "RW", "RM"}
all = {frozenset(central), frozenset(left_flank), frozenset(right_flank), frozenset({"LB", "LWB"}), frozenset({"RB", "RWB"})}
positions = {}
for i in all:
    for j in i:
        positions[j] = {k for k in i if k != j}
positions["CB"] = set()
positions["GK"] = set()

lowest_positions = {"ST":"CDM", "CF":"CDM", "CAM":"CDM", "CM":"CDM", "CDM":"CDM", "LW":"LM", "LF":"LM", "LM":"LM", "RW":"RM", "RF":"RM", "RM":"RM", "CB":"CB",
                    "GK":"GK", "LWB":"LB", "LB":"LB", "RWB":"RB", "RB":"RB"}
alternate_positions = {"LB" : {"LW", "LM", "CB"}, "RB" : {"RW", "RM", "CB"}, "CDM": {"CB", "LF", "RF", "RM", "LM"}, "CB": {"CDM", "LB", "RB"},
                       "LM": {"CM", "LWB", "LB", "RM"}, "RM":{"CM", "RWB", "RB", "LM"}}

simplified_positions = {"LCM": "CM", "RCM": "CM", "RDM": "CDM", "LDM": "CDM", "RCB":"CB", "LCB":"CB", "LST":"ST", "RST": "ST", "GK":"GK"}
FULL_CHEM = 10
OUT_OF_POSITION = 6
NO_CHEM = 1
TWO_CHEM = 2
THREE_CHEM = 3
STILL_GOOD = 7
OKAY_CHEM = 4

#LOYALTY ASSUMED, MANAGER NOT ASSUMED
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
        val = sum([i[1] for i in self.links])/ len(self.links)


        try:
            temp = lowest_positions[simplified_positions[self.pos]]

        except KeyError:
            temp = lowest_positions[self.pos]


        try:
            playin_temp = lowest_positions[simplified_positions[self.playing_pos]]
        except KeyError:
            playin_temp = lowest_positions[self.playing_pos]
        if val >= 1:
            if temp == playin_temp or temp in positions[playin_temp]:
                self.chem = FULL_CHEM
            elif playin_temp in alternate_positions[temp]:
                self.chem = OUT_OF_POSITION
            else:
                self.chem = THREE_CHEM
        elif 0.3 <= val < 1:
            if temp == playin_temp or temp in positions[playin_temp]:
                self.chem = STILL_GOOD
            elif playin_temp in alternate_positions[temp]:
                self.chem = OKAY_CHEM
            else:
                self.chem = TWO_CHEM
        elif val < 0.3:
            if temp == playin_temp or temp in positions[playin_temp]:
                self.chem = OKAY_CHEM
            elif playin_temp in alternate_positions[temp]:
                self.chem = TWO_CHEM
            else:
                self.chem = NO_CHEM


    def __str__(self):
        return "-".join([self.pos, self.playing_pos, self.nation, self.league, self.club, str(self.chem)])

