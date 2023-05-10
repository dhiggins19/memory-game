import random

# Defining a function which will randomize a list of animal emojis. These will be used as the pictures to be matched in the memory game.
def get_random_cards():
    chosen_cards = 0
    # Providing a list of unicode to print animal face emojis from https://unicode.org/emoji/charts/emoji-list.html Source: https://medium.com/analytics-vidhya/how-to-print-emojis-using-python-2e4f93443f7e
    animal_unicode = ['\U0001F435', '\U0001F436', '\U0001F43A', '\U0001F98A', '\U0001F431', '\U0001F981', '\U0001F42F', '\U0001F434']
    # Double the elements in the animal_unicode list, so there are matching pairs of emojis.
    animal_unicode *= 2 
    # Creating empty list which will be filled randomly selected elements from the animal_unicode list.
    card_selected = []
    while chosen_cards < 16:
        # Pick a random elements in the animal_unicode list. Source: https://docs.python.org/3/library/random.html#random.choice
        card_selection_options = random.choice(animal_unicode)
        # Add that selected element to the selected list.
        card_selected += card_selection_options
        # Remove the selected element from the options list.
        animal_unicode.remove(card_selection_options)
        chosen_cards +=1
    return card_selected

# Defining a function that will map the front and backs of the cards after the sequence has been randomized.
def answer_dict(animal_answers):
    # Creating empty dictionary to incrementally fill.
    board_dict = {}
    # Limiting loop to incrementing 16 times.
    for key_numbers in range(0,16):
        # Create the keys in board_dict based on the increment number (+ 1:0>2 so it matches the card numbers and their formatting) and set them equal to the corresponding index for the animal_emoji list.
        board_dict[f'{key_numbers + 1:0>2}'] = animal_answers[key_numbers]
    return board_dict