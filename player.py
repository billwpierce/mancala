from board import *

class Player():
    def __init__(self) -> None:
        pass

    def choose_move(self, board: Board) -> int:
        pass

class HumanPlayer(Player):
    def choose_move(self, board: Board) -> int:
        print(board)
        return int(input("Choose a move: "))
