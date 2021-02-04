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

