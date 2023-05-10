# Defining the funtion which will draw a single row for the 4 row board. Adding empty placeholder values to start.
def draw_row(top='', middle='', middle_content='', bottom=''):
    iteration = 0
    while iteration < 4:
        # The top portion of the row draws a ' ____' each iteration.
        top += f' {"_" * 4}'
        # The upper middle portion of the row draws a '|    ' each iteration.
        middle += f'|{" " * 4}'
        # The middle portion of the row (which will have the numbers and animal pictures) draws a '| -- ' with each iteration. The '--' will be replaced when the board is filled.
        middle_content += (f'| -- ')
        # The lower middle/bottom portion of the row draws a '|____' with each iteration.
        bottom += f'|{"_" * 4}'
        iteration += 1
    # I couldn't figure out a way to add the final characters/spaces to the row portions in the while loop. They are added after.
    top = f'{top:^27}'
    middle = f'{middle + "|":^27}'
    middle_content = f'{middle_content + "|":^27}'
    bottom = f'{bottom + "|":^27}'
    return [top, middle, middle_content, bottom]

# Defining the function which takes the row portion inputs to draw a complete board.
def draw_board(row_top, row_middle, row_content, row_bottom):
    drawn_rows = 0
    # The top portion of the row is outside of the loop since it only needs to be drawn once.
    drawn_board = f'{row_top}'
    while drawn_rows < 4:
        # Draw the upper middle, lower, then bottom portions of the row. (The bottom portion in each iteration will serve as the top portion in the following iteration)
        drawn_board += f'\n{row_middle}\n{row_content}\n{row_bottom}'
        drawn_rows += 1
    return drawn_board

# Defining the function which will display the current score at the top.
def draw_score_board(player, computer, current):
    curent = current + "'s Turn"
    top_bottom = f' {"-" * 25} '
    middle = f'| Player:{player:^3}| Computer:{computer:^3}|'
    score_board = f'{top_bottom}\n{middle}\n{top_bottom}\n{curent:^27}'
    return score_board