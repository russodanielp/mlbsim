from teams import Team

# TODO: use partial to load a season of play_games
# TODO: make season_scheduler function.  Should take a a league as input and create 162 game schedule.

class Season:
    def __init__(self, NL:League, AL:League):
        self.game_day = 0
        self.AL = AL
        self.NL = NL

    def play_game(self, home:Team, away:Team):
        total_win_percent = home.winning_prob() + away.winning_prob()
        home_win_percent = home.winning_prob() / total_win_percent
        away_win_percent = away.winning_prob() / total_win_percent
        import random
        outcome = random.uniform(0, 1)
        home.wins = home.wins + int(home_win_percent > outcome)
        home.losses = home.losses + int(home_win_percent < outcome)
        away.wins = away.wins + int(away_win_percent > outcome)
        away.losses = away.losses + int(away_win_percent < outcome)


    def play_season(self):
        for home_tm in self.AL.east:
            for away_tm in self.AL.central + self.AL.west:
                for game in range(3): self.play_game(home_tm, away_tm)

        for home_tm in self.AL.central:
            for away_tm in self.AL.east + self.AL.west:
                for game in range(3): self.play_game(home_tm, away_tm)

        for home_tm in self.AL.west:
            for away_tm in self.AL.central + self.AL.east:
                for game in range(3): self.play_game(home_tm, away_tm)

        for away_tm in self.AL.east:
            for home_tm in self.AL.central + self.AL.west:
                for game in range(3): self.play_game(home_tm, away_tm)

        for away_tm in self.AL.central:
            for home_tm in self.AL.east + self.AL.west:
                for game in range(3): self.play_game(home_tm, away_tm)

        for away_tm in self.AL.west:
            for home_tm in self.AL.central + self.AL.east:
                for game in range(3): self.play_game(home_tm, away_tm)


