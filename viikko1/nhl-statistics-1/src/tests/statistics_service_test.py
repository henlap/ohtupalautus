import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 57),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name,"Kurri")

    def test_search_nonexistent_player(self):
        player = self.stats.search("Selanne")
        self.assertEqual(player,None)

    def test_team(self):
        playerlist = self.stats.team("EDM")
        self.assertEqual(len(playerlist),3)

    def test_top(self):
        playerlist = self.stats.top(4)
        self.assertEqual(playerlist[0].goals,35)

    def test_enum_goals(self):
        playerlist = self.stats.top(4, SortBy.GOALS)
        self.assertEqual(playerlist[0].name,"Lemieux")

    def test_enum_assists(self):
        playerlist = self.stats.top(4, SortBy.ASSISTS)
        self.assertEqual(playerlist[1].name,"Yzerman")
    