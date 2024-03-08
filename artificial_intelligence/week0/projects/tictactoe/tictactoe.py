"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")

    if action not in actions(board):
        raise Exception("Invalid action")

    new_board = [row[:] for row in board]

    (y, x) = action
    symbol = player(board)
    new_board[y][x] = symbol
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for i, row in enumerate(board):
        for j, col in enumerate(board):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_symbol = winner(board)
    if winning_symbol == X:
        return 1
    elif winning_symbol == O:
        return -1
    else:
        return 0


def min_value(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for a in actions(state):
        v = min(v, max_value(result(state, a)))
    return v


def max_value(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for a in actions(state):
        v = max(v, min_value(result(state, a)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    playing_symbol = player(board)
    if playing_symbol == O:
        v = math.inf
        best_move = None
        for a in actions(board):
            if utility(result(board, a)) == -1:
                return a
            val = max_value(result(board, a))
            if val <= v:
                best_move = a
                v = val
        return best_move
    elif playing_symbol == X:
        v = -math.inf
        best_move = None
        for a in actions(board):
            if utility(result(board, a)) == 1:
                return a
            val = min_value(result(board, a))
            if val >= v:
                best_move = a
                v = val
        return best_move
    else:
        raise Exception("This should be impossible")
