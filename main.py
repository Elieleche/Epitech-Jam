from morpion import MorpionGame
from snake import SnakeGame
from connect_4 import Connect4
from puzzle import Puzzle

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

    game = Connect4()
    game.run()

    game = Puzzle()
    game.run()
