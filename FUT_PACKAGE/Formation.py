from .Players import Player
import os

dir = os.path.dirname(__file__)
class Formation:
    def __init__(self, name):
        self.team_chem = 0
        self.players = [None] * 11
        self.name = name
        file_path = os.path.join(dir, "Formations/" + name + ".in")
        file = open(file_path, "r")
        self.formation = {}
        self.key = {}
        next(file)
        count = 0
        for line in file:
                line = line.split()
                self.key[line[0]] = (count, line[1:])
                count += 1
        file.close()
    def put_players_from_file(self, filename):
        file = open(os.path.join(dir, filename), "r")
        for line in file:
            temp = line.split(',')
            self.players[self.key[temp[1]][0]] = Player(temp[0], temp[1], temp[2], temp[3], temp[4])
        file.close()
        for i in range(11):
            for j in self.key[self.players[i].playing_pos][1]:
                #todo: check icon to icon
                #red -> 0, yellow -> 1, green -> 2, hyperlink -> 3
                chem = 1

                if self.players[i].league == "icon" or self.players[self.key[j][0]].league == "icon":
                    if self.players[i].nation == self.players[self.key[j][0]].nation or\
                            self.players[i].club == self.players[self.key[j][0]].club:
                        chem += 1
                elif self.players[i].league == self.players[self.key[j][0]].league :
                    if bool(self.players[i].nation == self.players[self.key[j][0]].nation) ^ bool(self.players[i].club == self.players[self.key[j][0]].club):
                        chem += 1
                    elif self.players[i].club == self.players[self.key[j][0]].club and self.players[i].nation == self.players[self.key[j][0]].nation :
                        chem += 2
                elif self.players[i].nation != self.players[self.key[j][0]].nation and ( self.players[i].league != "icon" or self.players[self.key[j][0]].league != "icon"):
                    chem -= 1
                self.players[i].links.append((self.players[self.key[j][0]], chem))
        for i in self.players:
            i.calculate_chem()

            self.team_chem += i.chem


    # def get_team_chem(self):
    #
    #
    #     return sum([i.chem for i in self.players])
    def __str__(self):
        ret = ""
        for i in self.key:
            ret += i +  "---- " +  str(self.key[i][0]) + " " + " ".join(j for j in self.key[i][1])
            ret += "\n"
        return ret



test = Formation("433")
test.put_players_from_file("test.in")

print(test.team_chem)

