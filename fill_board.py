# Defining the function to replace the '--' in the drawn board argument with the list of animal emojis, provided as a second argument.
def draw_cards_front(board_front, animals):
    # For loop to loop through animal emoji list.
    for card_pictures in (animals):
        # Replace the first occurance of '--' with the incremental animal emoji in each iteration.
        board_front = board_front.replace('--', card_pictures, 1)
    # Return the board filled with emoji animals.
    return board_front

# Defining the function to replace the '--' in the drawn board argument with a range of numbers.
def draw_cards_back(board_back):
    # For loop to loop through all first occurances of '--' and replace it with an intrementally increasing number in the provided range.
    for card_numbers in range(1, 17):
        # Adding f-string formatting for consistent number formatting.
        board_back = board_back.replace('--', f'{card_numbers:0>2}', 1)
    # Return the board filled with numbers.
    return board_back