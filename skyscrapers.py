'''
This program is designed to find if there is a winning
combination on a game board.

https://github.com/shevdan/skyscrapers
'''

def read_input(path: str) -> list:
    """
    Read game board file from path.
    Return list of str.

    """

    with open(path) as file:
        board = []
        for line in file:
            line = line.rstrip()
            if not line:
                continue
            board.append(line)
    return board

def left_to_right_check(input_line: str, pivot: int) -> bool:
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.
`
    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = input_line[1:-1]
    flag = -1
    visible = 0
    for elem in input_line:
        height = int(elem)
        if height > flag:
            visible += 1
        flag = max(flag, height)

    if visible == pivot:
        return True
    return False



def check_not_finished_board(board: list) -> bool:
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*',\
         '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*',\
          '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if "?" in row:
            return False
    return True


def check_uniqueness_in_rows(board: list) -> bool:
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    """
    # getting rid of top and bottom rows containing no info about board
    board = board[1:-1]
    for row in board:
        row = row[1:-1]
        if len(row) != len(set(row)):
            return False
    return True


def check_horizontal_visibility(board: list) -> bool:
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    """

    for row in board[1:-1]:
        if row[0].isdigit():
            if not left_to_right_check(row, int(row[0])):
                return False
        if row[-1].isdigit():
            if not left_to_right_check(row[::-1], int(row[-1])):
                return False
    return True


def check_columns(board: list) -> bool:
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for elem in board[0]:
        if elem.isdigit():
            idx = board[0].index(elem)
            col = ''
            for row in board:
                col = col + row[idx]

            if len(col[1:-1]) != len(set(col[1:-1])):
                return False

            if not left_to_right_check(col, int(elem)):
                return False

    for elem in board[-1]:
        if elem.isdigit():
            idx = board[-1].index(elem)
            col = ''
            for i in reversed(range(len(board))):
                row = board[i]
                col += row[idx]

            if len(col[1:-1]) != len(set(col[1:-1])):
                return False

            if not left_to_right_check(col, int(elem)):
                return False

    return True


def check_skyscrapers(input_path: str) -> bool:
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    """

    board = read_input(input_path)
    if check_not_finished_board(board):
        if check_uniqueness_in_rows(board) and check_horizontal_visibility(board) and check_columns(board):
            return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
