from agents_dir.agents import *
from random import randint, choice

__all__ = ["ALL_MAPS"]


class VacuumMap1(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap1, self).__init__(8, 8)
        self.add_walls()
        self.dirty_all()
        self.start_from = (1, 2)


class VacuumMap2(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap2, self).__init__(8, 8)
        self.add_walls()
        self.dirty_all()
        self.add_thing(Wall(), (3, 2))
        self.add_thing(Wall(), (3, 3))


class VacuumMap3(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap3, self).__init__(4, 4)
        self.add_walls()
        self.dirty_all()
        self.add_thing(Wall(), (3, 1))
        self.add_thing(Wall(), (3, 2))


class VacuumMap4(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap4, self).__init__(10, 10)
        self.add_walls()
        self.dirty_all()
        self.add_thing(Wall(), (5, 3))
        self.add_thing(Wall(), (5, 4))
        self.add_thing(Wall(), (5, 5))
        self.add_thing(Wall(), (5, 6))
        self.add_thing(Wall(), (5, 7))
        self.add_thing(Wall(), (6, 3))
        self.add_thing(Wall(), (7, 3))
        self.add_thing(Wall(), (8, 3))


class VacuumMap5(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap5, self).__init__(10, 10)
        self.add_walls()
        self.dirty_all()
        self.add_thing(Wall(), (5, 3))
        self.add_thing(Wall(), (5, 4))
        self.add_thing(Wall(), (5, 5))
        self.add_thing(Wall(), (5, 6))
        self.add_thing(Wall(), (5, 7))
        self.add_thing(Wall(), (6, 3))
        self.add_thing(Wall(), (7, 3))
        self.add_thing(Wall(), (8, 3))
        self.add_thing(Wall(), (6, 7))
        self.add_thing(Wall(), (7, 7))
        self.add_thing(Wall(), (8, 7))


class VacuumMap6(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap6, self).__init__(8, 8)
        self.init_env(str('WWWWWWWW\nWWWDDWWW\nWDDDDDDW\nWDCCDDDW\nWWWDDWWW\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW'))
        self.start_from = (4, 4)


class VacuumMap7(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap7, self).__init__(8, 8)
        self.add_walls()
        self.dirty_all()
        self.add_thing(Wall(), (1, 1))
        self.add_thing(Wall(), (1, 4))
        self.add_thing(Wall(), (1, 5))
        self.add_thing(Wall(), (1, 6))
        self.add_thing(Wall(), (1, 7))
        self.add_thing(Wall(), (2, 1))
        self.add_thing(Wall(), (2, 4))
        self.add_thing(Wall(), (2, 5))
        self.add_thing(Wall(), (2, 6))
        self.add_thing(Wall(), (2, 7))
        self.add_thing(Wall(), (4, 1))
        self.add_thing(Wall(), (4, 4))
        self.add_thing(Wall(), (4, 5))
        self.add_thing(Wall(), (4, 6))
        self.add_thing(Wall(), (4, 7))
        self.add_thing(Wall(), (5, 1))
        self.add_thing(Wall(), (5, 2))
        self.add_thing(Wall(), (5, 4))
        self.add_thing(Wall(), (5, 5))
        self.add_thing(Wall(), (5, 6))
        self.add_thing(Wall(), (5, 7))
        self.add_thing(Wall(), (6, 1))
        self.add_thing(Wall(), (6, 2))
        self.add_thing(Wall(), (6, 4))
        self.add_thing(Wall(), (6, 5))
        self.add_thing(Wall(), (6, 6))
        self.add_thing(Wall(), (6, 7))
        self.add_thing(Wall(), (7, 1))
        self.add_thing(Wall(), (7, 2))
        self.add_thing(Wall(), (7, 4))
        self.add_thing(Wall(), (7, 5))
        self.add_thing(Wall(), (7, 6))
        self.add_thing(Wall(), (7, 7))
        self.start_from = (3, 1)


class VacuumMap8(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap8, self).__init__(8, 8)
        self.add_walls()
        self.dirty_all()
        self.add_thing(Wall(), (1, 4))
        self.add_thing(Wall(), (1, 5))
        self.add_thing(Wall(), (1, 6))
        self.add_thing(Wall(), (1, 7))
        self.add_thing(Wall(), (2, 1))
        self.add_thing(Wall(), (2, 4))
        self.add_thing(Wall(), (2, 5))
        self.add_thing(Wall(), (2, 6))
        self.add_thing(Wall(), (2, 7))
        self.add_thing(Wall(), (3, 1))
        self.add_thing(Wall(), (4, 1))
        self.add_thing(Wall(), (5, 1))
        self.add_thing(Wall(), (5, 2))
        self.add_thing(Wall(), (5, 3))
        self.add_thing(Wall(), (5, 4))
        self.add_thing(Wall(), (5, 5))


class VacuumMap9(VacuumEnvironment):

    def __init__(self):
        super(VacuumMap9, self).__init__(9, 9)
        self.add_walls()
        self.dirty_all()
        self.add_thing(Wall(), (1, 2))
        self.add_thing(Wall(), (1, 3))
        self.add_thing(Wall(), (1, 4))
        self.add_thing(Wall(), (1, 5))
        self.add_thing(Wall(), (1, 6))
        self.add_thing(Wall(), (2, 4))
        self.add_thing(Wall(), (2, 5))
        self.add_thing(Wall(), (2, 6))
        self.add_thing(Wall(), (3, 1))
        self.add_thing(Wall(), (3, 2))
        self.add_thing(Wall(), (3, 4))
        self.add_thing(Wall(), (3, 5))
        self.add_thing(Wall(), (3, 6))
        self.add_thing(Wall(), (4, 2))
        self.add_thing(Wall(), (4, 6))
        self.add_thing(Wall(), (5, 2))
        self.add_thing(Wall(), (5, 3))
        self.add_thing(Wall(), (5, 4))
        self.add_thing(Wall(), (5, 6))
        self.add_thing(Wall(), (6, 2))
        self.add_thing(Wall(), (6, 3))
        self.add_thing(Wall(), (7, 2))
        self.add_thing(Wall(), (7, 3))
        self.add_thing(Wall(), (7, 5))
        self.add_thing(Wall(), (7, 6))
        self.start_from = (2, 1)


class RandomMap(VacuumEnvironment):

    def __init__(self):
        l = randint(5, 10)
        super(RandomMap, self).__init__(l, l)

        # I create a matrix that I will use to make and manipulate the map
        matrix = [['W']*l for i in range(l)]

        # The first thing I'll put, excluded borders,
        # is 'Dirty places' in random places of the map
        for x in xrange(1, l-1):
            for y in xrange(1, l-1):
                if choice([0, 1]) == 0:
                    matrix[x][y] = 'D'

        # with this part of code i'll try to fix any possible point surrounded by walls
        for x in xrange(1, l-2):
            for y in xrange(1, l-2):
                if matrix[y][x] == 'D' or matrix[y][x-1] == 'W' or matrix[y][x+1] == 'W' or matrix[y+1][x] == 'W':
                    try:
                        if matrix[y][x+2] == 'D':
                            matrix[y][x+1] = 'D'
                        elif matrix[y][x-2] == 'D':
                            matrix[y][x-1] = 'D'
                        elif matrix[y+2][x] == 'D':
                            matrix[y+1][x] = 'D'
                        elif matrix[y-2][x] == 'D':
                            matrix[y-1][x] = 'D'
                    except IndexError:
                        pass

        # this is need for create the final string that the class 'VacuumEnvironment' takes
        string = ''
        for x in xrange(0, l):
            for y in xrange(0, l):
                string += matrix[x][y]
            string += '\n'

        self.init_env(string)
        self.string = string

        # Finally, I'm seeking a place where the robot can start
        var = 1
        row = 1
        for x in xrange(1, l):
            for y in xrange(1, l):
                if matrix[x][y] == 'D':
                    var, row = x, y
                    break

        self.start_from = (row, var)


class savedMap(VacuumEnvironment):

    def __init__(self):
        super(savedMap, self).__init__(8, 8)
        self.init_env(str('WWWWWWWW\nWWWDDWWW\nWDDDDDDW\nWDCCDDDW\nWWWDDWWW\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW'))
        self.start_from = (4, 4)
#
# All Maps TABLE
ALL_MAPS = {
    "VacuumMap1": VacuumMap1,
    "VacuumMap2": VacuumMap2,
    "VacuumMap3": VacuumMap3,
    "VacuumMap4": VacuumMap4,
    "VacuumMap5": VacuumMap5,
    "VacuumMap6": VacuumMap6,
    "VacuumMap7": VacuumMap7,
    "VacuumMap8": VacuumMap8,
    "VacuumMap9": VacuumMap9,
    "RandomMap": RandomMap,
    "savedMap": savedMap
}
