from teams import Team

AL_EAST = list(map(lambda x: Team(x[0], x[1]), {
    "Boston Red Sox":0.8,
    "Tampa Bay Rays":0.4,
    "New York Yankees":0.6,
    "Baltimore Orioles":0.7,
    "Toronto Blue Jays":0.7
}))

AL_CENTRAL = list(map(lambda x: Team(x[0], x[1]), {
    "Detroit Tigers":0.6,
    "Clevland Indians":0.6,
    "Kansas City Royals":0.5,
    "Chicago White Sox":0.4,
    "Minnesota Twins":0.3
}))

AL_WEST = list(map(lambda x: Team(x[0], x[1]), {
    "Texas Rangers":0.7,
    "Seattle Mariners":0.6,
    "Houston Astros":0.3,
    "Los Angeles Angels of Anaheim":0.2,
    "Oakland Athletic":0.1
}))

class League:
    def __init__(self, name:str, east:list, central:list, west:list):
        self.name = name
        self.east = east
        self.central = central
        self.west = west

class NationalLeague(League):
    def __init__(self):
        #self.League('NL', NL_EAST, NL_CENTRAL, NL_WEST)
        pass


class AmericanLeague(League):
    def __init__(self):
        self.League('AL', AL_EAST, AL_CENTRAL, AL_WEST)



