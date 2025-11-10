from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://cdn.nba.com/static/json/liveData"
ALL_JSON = "/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    scoreboard = data['scoreboard']
    games = scoreboard['games']
    for game in games:
        home_team = game['homeTeam']
        away_team = game['awayTeam']
        clock = game['gameClock']
        period = game['period']
        print('========================')
        print(f"{home_team['teamTricode']} vs {away_team['teamTricode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period}")
        
get_links()
