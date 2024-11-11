import requests
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)
    
    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    sorted_players = sorted(
            players,
            reverse=True,
            key= lambda p: (p.points, p.goals)
        )

    print("Players from FIN:\n")
    
    for player in sorted_players:
        if player.nation == "FIN":
            print(player)

if __name__ == "__main__":
    main()
