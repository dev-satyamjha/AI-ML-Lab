HUMAN = "X"
AI = "O"
EMPTY = " "

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


def minimax(board, is_ai):
    if winner(board, AI):
        return 1
    if winner(board, HUMAN):
        return -1
    if EMPTY not in board:
        return 0

    if is_ai:
        best = -100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best = max(best, minimax(board, False))
                board[i] = EMPTY
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                best = min(best, minimax(board, True))
                board[i] = EMPTY
        return best


def ai_move(board):
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move


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

        if EMPTY not in board:
            print("Draw!")
            break

        board[ai_move(board)] = AI

        if winner(board, AI):
            display(board)
            print("AI wins!")
            break


play()