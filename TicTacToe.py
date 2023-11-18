# import random
# import ast
# import shutil
# from os import system, name
#
#
# class DrawGameBoard:
#     def __int__(self, move):
#         self.move = move
#
#     def set_move(self, move):
#         self.move = move
#
#     def get_move(self):
#         return self.move
#
#     def game_board(self):
#         """
#         5X5 game board
#         :return:
#         """
#         game_board = [[' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
#                       ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
#                       [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
#                       ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
#                       [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
#                       ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
#                       [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' '],
#                       ['-', '+', '-', '+', '-', '+', '-', '+', '-'],
#                       [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
#                       ]
#         return game_board
#
#     def print_game_board(self, game_board):
#         print("\n\n\n============================")
#         print("Tic Tac Toe, two player game:")
#         print("============================\n")
#         for i in range(len(game_board)):
#             for j in range(len(game_board[i])):
#                 print(game_board[i][j], end=" ")
#             print()
#
#     def is_move_available(self, current_moves_list, move_picked):
#         """
#         Checks if the move the human have selected is still
#         int the list of available moves and returns True or False.
#         :param current_moves_list:
#         :param move_picked:
#         :return:
#         """
#         if move_picked in current_moves_list:
#             return True
#         return False
#
#     def pick_move(self, game_moves_list):
#         """
#         Human is asked to pick a move from the list
#         of available moves. Only a number in the list
#         of available moves gets validated.
#         The user is prompted until the right and available
#         move is chosen.
#         :param game_moves_list:
#         :return:
#         """
#         print("\nChoose a move from the list of available moves above:")
#         my_chosen_move = input()
#         while not my_chosen_move.isdigit() or int(my_chosen_move) not in game_moves_list or (
#                 int(my_chosen_move) < 1 or int(my_chosen_move) > 9):
#             print("\nTry again, choose a move from the list of available moves above:")
#             my_chosen_move = input()
#         return my_chosen_move
#
#     def get_file_length(self, file_name):
#         word_count = 0
#         with open(file_name, 'r') as file:
#             data = file.read()
#             lines = data.split()
#             for i in lines:
#                 word_count += 1
#         return word_count
#
#     def store_move_in_file(self, move_index, move_type):
#         """
#         :param move_index:
#         :param move_type:
#         :return:
#         store the move value X or O followed by the index
#         of the position of the move. Example 2:X
#         """
#
#         file_name = "tictactoe.txt"
#         move_value_and_type = str(move_index) + ":" + str(move_type)
#         file_length = self.get_file_length(file_name)
#         file_length = int(file_length)
#         try:
#             file_name = open(file_name, 'a')
#             if file_length > 0:
#                 file_name.write(", ")
#                 file_name.write(move_value_and_type)
#             else:
#                 file_name.write(move_value_and_type)
#             file_name.close()
#         except Exception as e:
#             print("Error: ", e)
#
#     def update_game_moves(self, remove_move, moves_list, player_type):
#         """
#         Once the computer or the human selects a valid move,
#         the moves list gets updated by removing that move from
#         the list to make sure on move is not made twice.
#         :param remove_move:
#         :param moves_list:
#         :param player_type:
#         :return: update moves list
#         """
#         remove_move = int(remove_move)
#
#         if len(moves_list) < 1:
#             return moves_list
#
#         is_move_in_list = self.is_move_available(moves_list, remove_move)
#
#         if player_type == "human":
#             print("Is move human chose in list: ", is_move_in_list)
#         else:
#             print("Is move computer chose in list: ", is_move_in_list)
#
#         if is_move_in_list or len(moves_list) == 1:
#             moves_list.remove(remove_move)
#             print("Moves available: ", moves_list)
#             return moves_list
#         else:
#             print("Try again, move provided has been played")
#             # pick_move()
#         return moves_list
#
#     def fill_played_position(self, game_board, position, game_letter):
#         """
#         Fills the chosen cell once a human or computer
#         makes a move.
#         :param game_board:
#         :param position:
#         :param game_letter:
#         :return: game board
#         """
#         for i in range(25):
#             if position == int(1):
#                 game_board[0][0] = game_letter
#                 break
#             elif position == int(2):
#                 game_board[0][2] = game_letter
#                 break
#             elif position == int(3):
#                 game_board[0][4] = game_letter
#                 break
#             elif position == int(4):
#                 game_board[0][6] = game_letter
#                 break
#             elif position == int(5):
#                 game_board[0][8] = game_letter
#                 break
#             elif position == 6:
#                 game_board[2][0] = game_letter
#                 break
#             elif position == int(7):
#                 game_board[2][2] = game_letter
#                 break
#             elif position == int(8):
#                 game_board[2][4] = game_letter
#                 break
#             elif position == int(9):
#                 game_board[2][6] = game_letter
#                 break
#             elif position == int(10):
#                 game_board[2][9] = game_letter
#                 break
#             elif position == int(11):
#                 game_board[4][0] = game_letter
#                 break
#             elif position == int(12):
#                 game_board[4][2] = game_letter
#                 break
#             elif position == int(13):
#                 game_board[4][4] = game_letter
#                 break
#             elif position == int(14):
#                 game_board[4][6] = game_letter
#                 break
#             elif position == int(15):
#                 game_board[4][8] = game_letter
#                 break
#             elif position == int(16):
#                 game_board[6][0] = game_letter
#                 break
#             elif position == int(17):
#                 game_board[6][2] = game_letter
#                 break
#             elif position == int(18):
#                 game_board[6][4] = game_letter
#                 break
#             elif position == int(19):
#                 game_board[6][6] = game_letter
#                 break
#             elif position == int(20):
#                 game_board[6][8] = game_letter
#                 break
#             elif position == int(21):
#                 game_board[8][0] = game_letter
#                 break
#             elif position == int(22):
#                 game_board[8][2] = game_letter
#                 break
#             elif position == int(23):
#                 game_board[8][4] = game_letter
#                 break
#             elif position == int(24):
#                 game_board[8][6] = game_letter
#                 break
#             elif position == int(25):
#                 game_board[8][8] = game_letter
#                 break
#         return game_board
#
#     def clear_old_console_output(self):
#         """
#         clear the old console outputs to
#         print upto date output and keep
#         a clean game view.
#         :return:
#         """
#         # clear windows console
#         if name == 'nt':
#             _ = system('cls')
#         else:
#             # clear Mac or linux console output
#             _ = system('clear')
#
#
# if __name__ == '__main__':
#     initial_game_moves = [1, 2, 3, 4, 5,
#                           6, 7, 8, 9, 10,
#                           11, 12, 13, 14, 15,
#                           16, 17, 18, 19, 20,
#                           21, 22, 23, 24, 25]
#
#     move_one = DrawGameBoard()
#     move_one.clear_old_console_output()
#     move_one.set_move("set")
#     print(f"Move one is --- {move_one.get_move()}")
#     move_one.print_game_board(move_one.game_board())
