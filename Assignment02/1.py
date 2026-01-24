def display_board(board: list[str]) -> None:
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board: list[str], player: str) -> bool:
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(
        all(board[i] == player for i in condition) for condition in win_conditions
    )


def is_draw(board: list[str]) -> bool:
    return all(cell != " " for cell in board)


def get_move(player: str, board: list[str]) -> int:
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position. Choose between 1 and 9.")
            elif board[move] != " ":
                print("Position already chosen. Choose another position.")
            else:
                return move
        except ValueError:
            print("Please enter a number.")


def play_tic_tac_toe() -> None:
    board = [" "] * 9
    current_player = "X"

    print("TIC-TAC-TOE (2 Player)")
    print("Positions are numbered 1 to 9 as follows:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

    while True:
        display_board(board)
        move = get_move(current_player, board)
        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_tic_tac_toe()