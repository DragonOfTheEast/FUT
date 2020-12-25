from FUT_PACKAGE.Players import Player


class Formation:
    def __init__(self, name):
        self.name = name
        formation = name+".in"
        file = open("Formations/"+formation, "r")
        self.formation = {}
        self.key = {}
        next(file)
        count = 1
        for line in file:
            if line[0] not in self.key:
                self.key[line[0]] = (count, line[1:].split())
                count += 1
        file.close()
        file = open("Formations/" + formation, "r")
        next(file)

        for line in file:
            teem = Player(self.key[line[0]], )



