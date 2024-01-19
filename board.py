from player import *

class Board:
    # Player 0 is Left Score, Top Row
    # Player 1 is Right Score, Bottom Row
    # Tiles move counter-clockwise
    def __init__(self, top_pits = [4 for i in range(6)], bot_pits = [4 for i in range(6)], stores = [0 for i in range(2)]):
        self.top_pits = top_pits
        self.bot_pits = bot_pits
        self.stores = stores
    
    def get_flipped_board(self) -> 'Board':
        return Board(list(reversed(self.bot_pits)), list(reversed(self.top_pits)), list(reversed(self.stores)))
    
    def __repr__(self) -> str:
        return "{ls} {tr} {rs}\n{ls} {br} {rs}".format(ls=str(self.stores[0]), rs=str(self.stores[1]), tr=str(self.top_pits), br=str(self.bot_pits))
    
    def update_pit(self, position, amount: int, val_not_slope:bool=False):
        if position[0] == 0:
            if val_not_slope:
                self.top_pits[position[1]] = amount
            else:
                self.top_pits[position[1]] += amount
        else: # bottom player
            if val_not_slope:
                self.bot_pits[5 - position[1]] = amount
            else:
                self.bot_pits[5 - position[1]] += amount

    def get_pit(self, position) -> int:
        if position[0] == 0:
            return self.top_pits[position[1]]
        else: # bottom player
            return self.bot_pits[5 - position[1]]

    
    def move(self, player_number: int, space_number: int) -> bool:
        # Space number goes 0-5, where 0 represents the closest to the score, 5 farthest.
        # TODO: Verify that the move is valid.
        print(f"Player {player_number} executing move from space {space_number}.")
        current_pos = [player_number, space_number]
        num_markers = self.get_pit(current_pos)
        self.update_pit(current_pos, 0, True)
        while num_markers > 0:
            if current_pos[1] == 0:
                if current_pos[0] == player_number:
                    self.stores[player_number] += 1
                    current_pos[1] = -1
                else:
                    current_pos = [int(not(current_pos[0])), 5]
                    self.update_pit(current_pos, 1)
            else: 
                if current_pos[1] == -1:
                    current_pos = [int(not(current_pos[0])), 5]
                else:
                    current_pos[1] = current_pos[1] - 1
                self.update_pit(current_pos, 1)
            num_markers -= 1
        if current_pos[1] == -1:
            return True # returns True if scored on last turn!
        elif self.get_pit(current_pos) == 1:
            self.update_pit(current_pos, -1)
            self.stores[player_number] += 1 + self.get_pit([int(not(player_number)), 5 - current_pos[1]])
            self.update_pit([int(not(player_number)), 5 - current_pos[1]], 0, True)
        return False
    
    def play_game(self, player_zero, player_one):
        curr_player_num = 0
        while sum(self.stores) < 48:
            rep = False
            if curr_player_num == 0:
                mv = player_zero.choose_move(self)
                rep = self.move(curr_player_num, mv)
            else:
                mv = player_one.choose_move(self.get_flipped_board())
                rep = self.move(curr_player_num, mv)
            if not rep:
                curr_player_num = int(not(curr_player_num))
        if self.stores[0] == self.stores[1]:
            print("The game ends in a tie!")
            return -1
        else:
            print(f"With scores of {self.stores}, the winner is player {'zero' if self.stores[0] > self.stores[1] else 'one'}")
            return 0 if self.stores[0] > self.stores[1] else 1
                


if __name__ == "__main__":
    board = Board()
    player_zero = RandomPlayer()
    player_one = RandomPlayer()
    board.play_game(player_zero, player_one)