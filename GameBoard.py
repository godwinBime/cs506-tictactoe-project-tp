import random
import ast
import shutil
from os import system, name


class DrawGameBoard:
    def __int__(self, move):
        self.move = move

    def set_move(self, move):
        self.move = move

    def get_move(self):
        return self.move

    def game_board(self):
        game_board = [[' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
                      ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
                      [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
                      ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
                      [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
                      ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
                      [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
                      ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
                      [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
                      ]
        return game_board

    def print_game_board(self, game_board):
        print("\n\n\n============================")
        print("Tic Tac Toe, two player game:")
        print("============================\n")
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                print(game_board[i][j], end=" ")
            print()

    def clear_old_console_output(self):
        """
        clear the old console outputs to
        print upto date output and keep
        a clean game view.
        :return:
        """
        # clear windows console
        if name == 'nt':
            _ = system('cls')
        else:
            # clear Mac or linux console output
            _ = system('clear')


if __name__ == '__main__':
    initial_game_moves = [1, 2, 3, 4, 5,
                          6, 7, 8, 9, 10,
                          11, 12, 13, 14, 15,
                          16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25]

    move_one = DrawGameBoard()
    move_one.set_move("set")
    print(f"Move one is --- {move_one.get_move()}")
    move_one.print_game_board(move_one.game_board())
