from .Players import Player
import os

dir = os.path.dirname(__file__)
class Formation:
    def __init__(self, name):
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
        players = [None] * 11
        for line in file:
            temp = line.split(',')
            players[self.key[temp[1]][0]] = Player(temp[0], temp[1], temp[2], temp[3], temp[4])
        file.close()
        for i in range(11):
            for j in self.key[players[i].playing_pos][1]:
                #todo: do links
                #red -> -1, yellow -> 0, green -> 1, hyperlink -> 2
                chem = 0

                if players[i].league == "icon" or players[self.key[j][0]].league == "icon":
                    if players[i].nation == players[self.key[j][0]].nation or\
                            players[i].club == players[self.key[j][0]].club:
                        chem += 1
                elif players[i].league == players[self.key[j][0]].league :
                    if bool(players[i].nation == players[self.key[j][0]].nation) ^ bool(players[i].club == players[self.key[j][0]].club):
                        chem += 1
                    elif players[i].club == players[self.key[j][0]].club and players[i].nation == players[self.key[j][0]].nation :
                        chem += 2
                elif players[i].nation != players[self.key[j][0]].nation and ( players[i].league != "icon" or players[self.key[j][0]].league != "icon"):
                    chem -= 1
                players[i].links.append((players[self.key[j][0]], chem))
        for i in players:
            print(i.playing_pos, end=" ")
            for j in i.links:
                print(j[0].playing_pos+ "--",  j[1], end=" ")
            print()
        # for line in file:
        #     playing_pos = line.split(',')[1]
        #     temp = line.split(',')
        #     self.formation[self.key[playing_pos][0]] = Player(temp[0], temp[1], temp[2], temp[3], temp[4])

    def __str__(self):
        ret = ""
        for i in self.key:
            ret += i +  "---- " +  str(self.key[i][0]) + " " + " ".join(j for j in self.key[i][1])
            ret += "\n"

        return ret



test = Formation("433")
test.put_players_from_file("test.in")

