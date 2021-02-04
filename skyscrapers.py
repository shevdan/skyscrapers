'''
This program is designed to find if there is a winning
combination on a game board.

https://github.com/shevdan/skyscrapers
'''

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path) as file:
        board = []
        for line in file:
            line = line.rstrip()
            if not line:
                continue
            board.append(line)
    return board

        
def left_to_right_check(input_line: str, pivot: int):
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
    for idx in range(pivot):
        height = int(input_line[idx])
        if height <= flag:
            return False
        flag = height
    return True

