class Team:
    def __init__(self, team_name:str, winning_prob:float):
        self.team_name = team_name
        self.winning_prob = winning_prob
        self.wins = 0
        self.losses = 0
        self.games_played = 0

    def get_record(self):
        return "{0} Wins, {1} Losses".format(self.wins, self.losses)

    def __str__(self):
        return self.team_name

    def __repr__(self):
        return self.__str__()

