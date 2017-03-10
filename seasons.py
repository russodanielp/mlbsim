
""" module to load seasons from game logs """
import os
import pandas as pd
from teams import Team, play_game

# game log dir

GL_DIR = os.getenv('MLB_DATA')
if not GL_DIR:
    raise Exception("There is no MLB_DATA environmental variable set.")

class Game:

    def __init__(self, home_team, away_team, home_score, away_score):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score


class Season:

    def __init__(self, year, games):
        self.year = year
        self.games = games
        # dictionary where teams are keys, values are [wins]
        self.standings = {}


    def play_season(self):
        for game in self.games:
            home_record = self.standings.get(game.home_team, [0, 0])
            away_record = self.standings.get(game.away_team, [0, 0])
            if game.away_score > game.home_score:
                away_record[0] += 1
                home_record[1] += 1
                self.standings[game.away_team] = away_record
                self.standings[game.home_team] = home_record
            else:
                home_record[0] += 1
                away_record[1] += 1
                self.standings[game.home_team] = home_record
                self.standings[game.away_team] = away_record




def load_season(year):
    """ Return a Season object, by parsing through game log file """
    path = GL_DIR + "\\game_logs\\GL{0}.txt".format(year)
    season_info = pd.read_csv(path, index_col=0, header=None)
    games = []
    for game, info in season_info.iterrows():
        away_team = info[3]
        home_team = info[6]
        away_score = info[9]
        home_score = info[10]
        games.append(Game(home_team, away_team, home_score, away_score))
    return Season(year, games)

def fake_season(year):
    teams = {}
    season = load_season(year)
    season.play_season()
    print(season.standings)
    for t, record in season.standings.items():
        win_percent = record[0] / record[1]
        teams[t] = Team(t, win_percent)

    for game in season.games:
        play_game(teams[game.home_team], teams[game.away_team])

    records = {}
    for team, obj in teams.items():
        records[team] = obj.get_record()
    return records