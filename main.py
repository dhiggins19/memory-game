# Main Program File

# This is a memory game. It will output the directions and give the player options to guess.

# Importing the functions necessary to draw the board.
from draw_board import draw_row, draw_board, draw_score_board
# Importing the functions to fill in the cards on the board.
from fill_board import draw_cards_front, draw_cards_back
# Importing the functions to randomize the order of emojis for the cards
from random_selection import get_random_cards, answer_dict
# Importing the functions which take guess inputs, perform error checking, and update the board to reflect the guesses.
from guesses import player_guess, computer_guess, clear_screen, guess_check

# Draw the pieces of a row for the game board.
row_pieces = draw_row()

# Assemble the board from the pieces of the rows.
game_board = draw_board(row_pieces[0], row_pieces[1], row_pieces[2], row_pieces[3])

# Get a randomized list of 8 pairs of animal emojis, which will be used as the pictures to be matched.
random_animals = get_random_cards()

# Fill the front of the board (the board is composed of cards). The front was chosen to have the pictures. They are face-down.
board_front = draw_cards_front(game_board, random_animals)

# Fill in the back of the board. (the number side of the cards)
board_back = draw_cards_back(game_board)

# Create a dictionary matching the filled numbers and animal pictures.
answers = answer_dict(random_animals)

# Creating variables to track scores
player_score = 0
computer_score = 0

try:
    # Welcome message and player instructions
    print('This is a memory game that can be played in your console.\nNumbered cards will be layed out for you. Type the number to flip over a card.\nTry to find more matching pairs of cards than the computer.\nYou can press "ctrl + c" to quit at any time.\n')

    # Ask player to select a difficulty level
    level = 'invalid'
    while level == 'invalid':
        # Exception handling in place to catch invalid inputs.
        try:
            difficulty_level = int(input('1: Easy\n2: Medium\n3: Hard\n\nPlease enter the number to select a difficulty level: '))
            if (0 < difficulty_level < 4) == False:
                raise ValueError
            else:
                level = "valid"
        except ValueError:
            print('That is not a valid input. Please enter a number between 1-3.\n')

    if difficulty_level == 3:
        # Guess accuracy will be used in the computer guesses.
        guess_accuracy = .85
        # Print confirmation of selection for the player.
        print(f'\nYou have selected a hard level of difficulty. Good luck!')
    elif difficulty_level == 2:
        guess_accuracy = .4
        print(f'\nYou have selected a medium level of difficulty. Good luck!')
    else:
        guess_accuracy = .2
        print(f'\nYou have selected an easy level of difficulty. Good luck!')

    clear_screen(delay='long')

    # Set game loop exit variable
    game_ongoing = True
    # Start the game loop.
    while game_ongoing == True:
            # Set the player turn exit variable.
            player_turn = True
            # Start the player turn loop.
            while player_turn == True:
                if game_ongoing == False:
                    break
                player_guess_1 = player_guess(board_back, answers, player_score, computer_score)
                player_guess_2 = player_guess(player_guess_1[0], answers, player_score, computer_score, player_guess_1[1])
                print(draw_score_board(player_score, computer_score, 'Player'))
                print(player_guess_2[0])
                check_result = guess_check(player_guess_1[1], player_guess_2[1], answers, board_back, 'You get', player_score, computer_score)
                if check_result != None:
                    player_score += 1
                    if check_result == False:
                        game_ongoing = False
                    else:
                        board_back = check_result
                else:
                    print('\nNo matches here. End of your turn')
                    clear_screen(delay='long')
                    player_turn = False
            computer_turn = True
            while computer_turn == True:
                if game_ongoing == False:
                    break
                computer_guess_1 = computer_guess(board_back, answers, player_score, computer_score, guess_accuracy)
                computer_guess_2 = computer_guess(computer_guess_1[0], answers, player_score, computer_score, guess_accuracy, computer_guess_1[1])
                print(draw_score_board(player_score, computer_score, 'Computer'))
                print(computer_guess_2[0])
                check_result = guess_check(computer_guess_1[1], computer_guess_2[1], answers, board_back, 'The computer gets', player_score, computer_score)
                if check_result != None:
                    computer_score += 1
                    if check_result == False:
                        game_ongoing = False
                    else:
                        board_back = check_result
                else:
                    print("\nNo matches here. End of computer's turn.")
                    clear_screen(delay='long')
                    computer_turn = False
# Giving player an option to quit at any time. Source: https://stackoverflow.com/questions/25512319/python-terminating-your-program-at-any-time
except KeyboardInterrupt:
    print('\n\nThanks for playing!')

if player_score + computer_score == 8:
    # Created ASCII art with: https://patorjk.com/software/taag
    player_win = ['\n$$\     $$\                         $$\      $$\ $$\           $$\ ',
                    '\$$\   $$  |                        $$ | $\  $$ |\__|          $$ |',
                    ' \$$\ $$  /$$$$$$\  $$\   $$\       $$ |$$$\ $$ |$$\ $$$$$$$\  $$ |',
                    '  \$$$$  /$$  __$$\ $$ |  $$ |      $$ $$ $$\$$ |$$ |$$  __$$\ $$ |',
                    '   \$$  / $$ /  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ |$$ |  $$ |\__|',
                    '    $$ |  $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |$$ |  $$ |    ',
                    '    $$ |  \$$$$$$  |\$$$$$$  |      $$  /   \$$ |$$ |$$ |  $$ |$$\ ',
                    '    \__|   \______/  \______/       \__/     \__|\__|\__|  \__|\__|\n',
                    'Thanks for playing!']

    computer_win = ['\n $$$$$$\                                                $$\                               $$\      $$\ $$\                     $$\ ',
                '$$  __$$\                                               $$ |                              $$ | $\  $$ |\__|                    $$ |',
                '$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\   $$$$$$\        $$ |$$$\ $$ |$$\ $$$$$$$\   $$$$$$$\ $$ |',
                '$$ |      $$  __$$\ $$  _$$  _$$\ $$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\ $$  __$$\       $$ $$ $$\$$ |$$ |$$  __$$\ $$  _____|$$ |',
                '$$ |      $$ /  $$ |$$ / $$ / $$ |$$ /  $$ |$$ |  $$ |  $$ |    $$$$$$$$ |$$ |  \__|      $$$$  _$$$$ |$$ |$$ |  $$ |\$$$$$$\  \__|',
                '$$ |  $$\ $$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |  $$ |  $$ |$$\ $$   ____|$$ |            $$$  / \$$$ |$$ |$$ |  $$ | \____$$\     ',
                '\$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |            $$  /   \$$ |$$ |$$ |  $$ |$$$$$$$  |$$\ ',
                ' \______/  \______/ \__| \__| \__|$$  ____/  \______/    \____/  \_______|\__|            \__/     \__|\__|\__|  \__|\_______/ \__|',
                '                                  $$ |                                                                                             ',
                '                                  $$ |                                                                                             ',
                '                                  \__|                                                                                             \n',
                'Thanks for playing! Better luck next time :(']
    if player_score > computer_score:
        winner = player_win
    else:
        winner = computer_win

    for line in winner:
        print(line)