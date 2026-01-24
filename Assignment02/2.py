from collections import deque
from copy import deepcopy

HUMAN: str = "X"
AI: str = "O"
EMPTY: str = " "

WIN_COMBOS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def display(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("-----------")
    print()


def winner(board, player):
    return any(all(board[i] == player for i in combo) for combo in WIN_COMBOS)


def draw(board):
    return EMPTY not in board


def bfs_ai_move(board):
    queue = deque()
    queue.append((board, None))

    while queue:
        state, first_move = queue.popleft()

        if winner(state, AI):
            return first_move

        for i in range(9):
            if state[i] == EMPTY:
                new_state = deepcopy(state)
                new_state[i] = AI
                move = first_move if first_move is not None else i
                queue.append((new_state, move))

    for i in range(9):
        if board[i] == EMPTY:
            return i


def play():
    board = [EMPTY] * 9

    while True:
        display(board)

        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1

                if move < 0 or move > 8:
                    print("Please enter a number between 1 and 9.")
                    continue

                if board[move] != EMPTY:
                    print("The position is already taken.")
                    continue

                break

            except ValueError:
                print("Invalid input. Please enter a number.")

        board[move] = HUMAN

        if winner(board, HUMAN):
            display(board)
            print("You win!")
            break

        if draw(board):
            print("Draw!")
            break

        ai_move = bfs_ai_move(board)
        board[ai_move] = AI

        if winner(board, AI):
            display(board)
            print("AI wins!")
            break


play()