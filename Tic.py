import os.path
import random
from os import system, name


class ComputerMoves:
    def __init__(self, is_a_new_game):
        self.is_a_new_game = is_a_new_game

    def set_is_a_new_game(self, is_a_new_game):
        self.is_a_new_game = is_a_new_game

    def get_is_a_new_game(self):
        return self.is_a_new_game

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

    def format_gameboard_view(self, board):
        for i in range(5):
            row_str = ""
            for j in range(5):
                row_str += f" {board[i][j]} |"
            print(row_str[:-1])  # Remove the last '|' character
            if i < 4:
                print("-" * 19)

    def print_game_board(self, board):
        is_new_game = self.get_is_a_new_game()

        if is_new_game:
            self.set_is_a_new_game(False)
            self.format_gameboard_view(board)
        else:
            self.clear_old_console_output()
            print("\nAI just made a move.\nYour turn\n")
            self.format_gameboard_view(board)

    def get_file_length(self, file_name):
        word_count = 0
        is_file_exist = os.path.exists(file_name)
        if is_file_exist:
            with open(file_name, 'r') as file:
                data = file.read()
                lines = data.split()
                for i in lines:
                    word_count += 1
            return word_count
        print("File not found")
        return word_count

    def clean_file(self, file_to_clean):
        """
        When the game begins the text file storing
        game moves deletes moves from the previous
        game
        :return:
        """
        file_length = self.get_file_length(file_to_clean)
        if int(file_length) > 0:
            moves_file = open(file_to_clean, "w")
            moves_file.close()

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

    def who_will_go_first(self):
        return 'player' if random.randint(0, 1) == 0 else 'AI'

    def make_move(self, board, letter, move):
        board[move[0]][move[1]] = letter

    def check_winner(self, board, mark):
        for i in range(5):
            if all(board[i][j] == mark for j in range(5)) or all(board[j][i] == mark for j in range(5)):
                return True
        if all(board[i][i] == mark for i in range(5)) or all(board[i][4 - i] == mark for i in range(5)):
            return True
        return False

    def is_space_free(self, board, move):
        return board[move[0]][move[1]] == ' '

    def player_move(self, board):
        while True:
            try:
                move = int(input('Enter your move (1-25): '))
                if 1 <= move <= 25:
                    move_row = (move - 1) // 5
                    move_col = (move - 1) % 5
                    if self.is_space_free(board, (move_row, move_col)):
                        return move_row, move_col
                    else:
                        print('That position has already been occupied!')
                else:
                    print('Please input a number within the range of 1 to 25')
            except ValueError:
                print('Please enter a valid number!')

    def ai_move(self, board):
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if self.is_space_free(board, (row, col)):
                return row, col

    def is_board_full(self, board):
        return all(board[i][j] != ' ' for i in range(5) for j in range(5))

    def play_game(self):
        game = ComputerMoves(True)

        board = [[' ' for _ in range(5)] for _ in range(5)]

        while True:
            player = 'O'
            AI = 'X'
            turn = game.who_will_go_first()

            print("\nWelcome to the 5x5 Tic Tac Toe game!\n")
            print(f'The {turn} will go first.')

            while True:
                if turn == 'player':
                    game.print_game_board(board)
                    move_row, move_col = game.player_move(board)
                    game.make_move(board, player, (move_row, move_col))
                    game.print_game_board(board)

                    if game.check_winner(board, player):
                        print("Great job! You've conquered the game!")
                        return
                    elif game.is_board_full(board):
                        print('The game is a tie!')
                        return
                    else:
                        turn = 'AI'
                else:
                    move_row, move_col = game.ai_move(board)
                    game.make_move(board, AI, (move_row, move_col))
                    game.print_game_board(board)

                    if game.check_winner(board, AI):
                        print("The AI has emerged victorious! You've been defeated.")
                        return
                    elif game.is_board_full(board):
                        print('The game is a tie!')
                        return
                    else:
                        turn = 'player'


if __name__ == "__main__":
    start_game = ComputerMoves(True)
    start_game.clean_file("tictactoe.txt")
    start_game.clear_old_console_output()
    start_game.play_game()
