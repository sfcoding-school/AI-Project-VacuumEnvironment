from . agents import *

# 'GoNorth' # sinistra
# 'GoEast', # giu'
# 'GoWest # su
# 'GoSouth' #destra


class UlisseAgentClass(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.mondo = {(0, 0): 0}
        self.actions = ['GoNorth', 'GoWest', 'GoSouth', 'GoEast']  # ulisse 1
        self.coordAction = {'GoNorth': (0, -1), 'GoWest': (-1, 0), 'GoSouth': (0, 1), 'GoEast': (1, 0)}

        self.last_action = -1

        self.coord = (0, 0)  # coordinate iniziali
        self.lastCoord = ()

        self.boolean = False

        def stampa():
            min_x = 0
            for thing in self.mondo:
                if thing[0] < min_x:
                    min_x = thing[0]

            min_y = 0
            for thing in self.mondo:
                if thing[1] < min_y:
                    min_y = thing[1]

            matrix = [[0]*15 for i in range(15)]

            for thing in self.mondo:
                matrix[thing[0] - min_x][thing[1]-min_y] = self.mondo[thing]

            for x in xrange(0, 15):
                for y in xrange(0, 15):
                    print matrix[x][y],
                print

            print self.mondo
            a = raw_input()

        def program((status, bump)):

            # mappa 7 faccio poco, mappa 8 disastro

            if status == 'Dirty':
                return 'Suck'

            if bump == 'Bump':
                self.mondo[self.coord] = -1  # perch' e' un muro
                self.coord = self.lastCoord  # resetto la vecchia coordinata

            if self.coord in self.mondo:
                self.mondo[self.coord] += 1
            else:
                self.mondo[self.coord] = 1

            while self.mondo[self.coord] <= 5:
                # stampa()
                nextAction = self.actions[(self.mondo[self.coord] - 1) % 4]
                nextCoord = (self.coord[0] + self.coordAction[nextAction][0],  self.coord[1] + self.coordAction[nextAction][1])
                # non voglio andare in direzione da cui sono venuto
                # DA FARE
                if nextCoord in self.mondo:
                    if self.mondo[nextCoord] >= 3 or self.mondo[nextCoord] == -1:
                        self.mondo[self.coord] += 1
                    else:
                        self.lastCoord = self.coord
                        self.coord = nextCoord
                        return nextAction
                    if self.boolean is True and self.mondo[nextCoord] != -1:
                        self.mondo[nextCoord] -= 1
                        self.boolean = False
                else:
                    self.mondo[nextCoord] = 0
                    self.lastCoord = self.coord
                    self.coord = nextCoord
                    return nextAction

            self.boolean = True
            return 'NoOp'

            # # mappa 7 faccio poco, mappa 8 disastro

            # if status == 'Dirty':
            #     return 'Suck'

            # if bump == 'Bump':
            #     print "bump"
            #     self.mondo[self.coord] = -1  # perch' e' un muro
            #     self.coord = self.lastCoord  # resetto la vecchia coordinata

            # try:
            #     self.mondo[self.coord] += 1
            # except KeyError:
            #     self.mondo[self.coord] = 1
            #     print 'KeyError 1'

            # print self.mondo[self.coord]
            # nextAction = self.actions[(self.mondo[self.coord] - 1) % 4]
            # nextCoord = (self.coord[0] + self.coordAction[nextAction][0],  self.coord[1] + self.coordAction[nextAction][1])
            # try:
            #     if self.mondo[nextCoord] >= 3 or self.mondo[nextCoord] == -1:
            #         return 'NoOp'
            # except KeyError:
            #     self.mondo[nextCoord] = 0

            # print nextAction

            # self.lastCoord = self.coord
            # self.coord = nextCoord
            # return nextAction

        self.program = program
