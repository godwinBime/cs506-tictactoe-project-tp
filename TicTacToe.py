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

    def pick_move(self, game_moves_list):
        print("\nChoose a move from the list of available moves above:")
        my_chosen_move = input()
        while not my_chosen_move.isdigit() or int(my_chosen_move) not in game_moves_list or (
                int(my_chosen_move) < 1 or int(my_chosen_move) > 9):
            print("\nTry again, choose a move from the list of available moves above:")
            my_chosen_move = input()
        return my_chosen_move

    def get_file_length(self, file_name):
        word_count = 0
        with open(file_name, 'r') as file:
            data = file.read()
            lines = data.split()
            for i in lines:
                word_count += 1
        return word_count

    def store_move_in_file(self, move_index, move_type):
        """
        :param move_index:
        :param move_type:
        :return:
        store the move value X or O followed by the index
        of the position of the move. Example 2:X
        """

        file_name = "tictactoe.txt"
        move_value_and_type = str(move_index) + ":" + str(move_type)
        file_length = self.get_file_length(file_name)
        file_length = int(file_length)
        try:
            file_name = open(file_name, 'a')
            if file_length > 0:
                file_name.write(", ")
                file_name.write(move_value_and_type)
            else:
                file_name.write(move_value_and_type)
            file_name.close()
        except Exception as e:
            print("Error: ", e)


if __name__ == '__main__':
    initial_game_moves = [1, 2, 3, 4, 5,
                          6, 7, 8, 9, 10,
                          11, 12, 13, 14, 15,
                          16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25]

    move_one = DrawGameBoard()
    move_one.clear_old_console_output()
    move_one.set_move("set")
    print(f"Move one is --- {move_one.get_move()}")
    move_one.print_game_board(move_one.game_board())
