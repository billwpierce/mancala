from board import *
from board import Board
import random

class Player():
    def __init__(self) -> None:
        pass

    def choose_move(self, board: Board) -> int:
        print("WRONG TURN")
        pass

class HumanPlayer(Player):
    def choose_move(self, board: Board) -> int:
        print(board)
        return int(input("Choose a move: "))

class HighestValuePlayer(Player):
    def choose_move(self, board: Board) -> int:
        return max(enumerate(board.top_pits),key=lambda x: x[1])[0]

class RandomPlayer(Player):
    def choose_move(self, board: Board) -> int:
        return random.randint(0, 5)