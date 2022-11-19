from game import Game
from exceptions import  GameOverCroupierException, GameOverException, GameOverUserException

try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print("Wygral Gracz")
except GameOverUserException:
    print("wygral Krupier")

