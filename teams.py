class Team:
    def __init__(self, team_name:str, winning_prob:float):
        self.team_name = team_name
        self.winning_prob = winning_prob
        self.wins = 0
        self.losses = 0

    def get_record(self):
        return [self.wins, self.losses]

    def won_game(self):
        self.wins += 1

    def lost_game(self):
        self.losses += 1

    def __str__(self):
        return self.team_name

    def __repr__(self):
        return self.__str__()

def play_game(home_team, away_team):
    total_prob = home_team.winning_prob + away_team.winning_prob
    home_prob = home_team.winning_prob / total_prob
    #way_prob = away_team.winning_prob / total_prob
    import random
    game_outcome = random.uniform(0, 1)
    if home_prob >= game_outcome:
        home_team.won_game()
        away_team.lost_game()
    else:
        home_team.lost_game()
        away_team.won_game()