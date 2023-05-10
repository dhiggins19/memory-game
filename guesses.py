from draw_board import draw_score_board
import random
import os
import time

# Creating custom exception subclass. Referenced: https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
class GuessError(Exception):
    '''This exception will be raised if the player attempts to guess a card that has already been guessed.'''

# Clear console after player makes guesses. Should also work in a Mac or Linux environment. Referenced: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Adding time delay options to cls function.
def clear_screen(delay=''):
    if delay == 'long':
        time.sleep(3)
        cls()
    elif delay == 'short':
        time.sleep(1)
        cls()
    else:
        cls()

# Defining the function for player guesses.
def player_guess(board_state, answers, player_score, computer_score, first_guess=''):
    print(draw_score_board(player_score, computer_score, 'Player'))
    print(f'{board_state}\n')
    guess = 'invalid'
    while guess == 'invalid':
        # Exception handling in place to catch invalid inputs.
        try:
            if first_guess == '':
                players_guess = f'{input("Guess a card: "):0>2}'
            else:
                players_guess = f'{input("Guess another card: "):0>2}'
            if (0 < int(players_guess) < 17) == False:
                raise ValueError
            elif ((players_guess == first_guess) or (players_guess in solved_cards)):
                raise GuessError
            else:
                guess = "valid"
        except ValueError:
            print('\nThat is not a valid input. Please enter a number between 1-16.')
        # Using earlier defined GuessError subclass.
        except GuessError:
            print('\nThat card has been guessed already.')
    # Subtracting 1 from guess to align card number with answer index.
    computer_knowledge[int(players_guess) - 1] = answers[players_guess]
    # Using board_with_guess function to search/replace board card number with the animal emoji.
    board_state = board_with_guess(players_guess, board_state, answers)
    clear_screen()
    return [board_state, players_guess]

# Defining function to be used for computer guesses.
def computer_guess(comp_board_state, answers, player_score, computer_score, accuracy, first_guess=''):
    print(draw_score_board(player_score, computer_score, 'Computer'))
    print(comp_board_state)
    # This conditional branch is used for the computer's first guess.
    if first_guess == '':
        # Looping through the items in the computer_knowledge list. This should only contain cards that have been "flipped over".
        for possible_guesses in computer_knowledge:
            # If there is a match of animal emojis, then pick one.
            if ((len(possible_guesses) == 1) and (computer_knowledge.count(possible_guesses) == 2)):
                computer_guess = f'{computer_knowledge.index(possible_guesses) + 1:0>2}'
                break
            else:
                selection = 'invalid'
                while selection == 'invalid':
                    choice = random.choice(range(0,16))
                    # The computer can exit the while loop if it picks a card that has not already been flipped over or solved. (Solved will be replaced with '--' and have a length of 2.)
                    if len(computer_knowledge[choice]) == 0:
                        computer_guess = f'{choice + 1:0>2}'
                        selection = 'valid'
                    # Created second exit condition where computer can pick a card that has already been flipped over. Should only be used once all cards have been flipped over.
                    elif len(computer_knowledge[choice]) == 1:
                        computer_guess = f'{choice + 1:0>2}'
                        selection = 'valid'
    # This conditional branch is used for the second computer guess.
    elif first_guess != '':
        # Defining variable for the emoji associated with the first guess.
        first_guess_animal = computer_knowledge[int(first_guess) - 1]
        # Creating a copy of the computer_knowledge list.
        guess_2_knowledge = computer_knowledge[:]
        # Search replacing first guess value with '--' so it will not be gussed twice.
        guess_2_knowledge[int(first_guess) - 1] = '--'
        # This conditional uses a randomly selected number and compares it to the accuracy (determined by difficulty level) to determine if the computer skips the known match.
        if ((computer_knowledge.count(first_guess_animal) == 2) and (random.choice(range(1,101)) < (accuracy * 100))):
            # Using list comprehension to find the animal matching the first guess. This is searching a the guess_2_knowledge list. Referenced: https://stackoverflow.com/questions/22267241/how-to-find-the-index-of-the-nth-time-an-item-appears-in-a-list
                computer_guess = f"{[index for index, animal in enumerate(guess_2_knowledge) if animal == first_guess_animal][0] + 1:0>2}"
        else:
            selection = 'invalid'
            while selection == 'invalid':
                choice = random.choice(range(0,16))
                if len(guess_2_knowledge[choice]) != 2:
                    computer_guess = f'{choice + 1:0>2}'
                    selection = 'valid'
    computer_knowledge[int(computer_guess) - 1] = answers[computer_guess]
    comp_board_state = board_with_guess(computer_guess, comp_board_state, answers)
    clear_screen(delay='short')
    return [comp_board_state, computer_guess]

# Defining function to search/replace the board card number with the associated animal emoji. This represents fipping a card over.
def board_with_guess(guess_number, current_board, answers):
    board_after_guess = current_board.replace(guess_number, answers[guess_number])
    return board_after_guess

# Defining function to check whether guess 1 and guess 2 have the same animal emoji.
def guess_check(guess_1, guess_2, answers, check_board, current, player_score, computer_score):
        # If guess 1 and guess 2 have the same answer (animal).
        if answers[guess_1] == answers[guess_2]:
            # Replace the guess squares with '--' to indicate they have been solved.
            check_board = check_board.replace(guess_1, '--')
            check_board = check_board.replace(guess_2, '--')
            # Add the cards to the previously defined solved_cards list.
            solved_cards.extend([guess_1, guess_2])
            # Substitite guess 1 and 2 with -- in the computer_knowledge list. It's logic will only guess items with a length of 0 or 1.
            computer_knowledge[int(guess_1) -1] = '--'
            computer_knowledge[int(guess_2) -1] = '--'
            # Check if game is over. Using 7 because this is evaluated before the 8th point is awarded.
            if (computer_score + player_score) == 7:
                game_ongoing = False
                print(f"\nThat's a match!")
                clear_screen(delay='long')
                return game_ongoing
            else:
                print(f"\nThat's a match! {current} to go again.")
                clear_screen(delay='long')
                return check_board
        # If guess 1 and 2 are not a match, return none.
        else:
            return

# Creating list full of empty values. Values will be updated as guesses are made and guess will have indexes matching the answers.
computer_knowledge = ['','','','','','','','','','','','','','','','']

# Creating empty list that will be populated with card numbers when matches are found.
solved_cards = []