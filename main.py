BOARD_SIZE = 3

def print_board(board):
    print("  0 1 2")
    for i in range(BOARD_SIZE):
        row = f"{i} "
        for j in range(BOARD_SIZE):
            symbol = board[i][j] if board[i][j] is not None else "."
            row += symbol + "|" if j < BOARD_SIZE - 1 else symbol
        print(row)
    print()

def is_winner(board, player):
    # Check rows
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)):
            return True

    # Check columns
    for j in range(BOARD_SIZE):
        if all(board[i][j] == player for i in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True

    return False

def is_tie(board):
    return all(board[i][j] is not None for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

def play():
    board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    current_player = "X"

    while True:
        print_board(board)

        # Check for winner
        if is_winner(board, current_player):
            print(f"{current_player} venceu!")
            return

        # Check for tie
        if is_tie(board):
            print("Empate!")
            return

        # Ask for current player's move
        row, col = get_move(board, current_player)

        # Make the move
        board[row][col] = current_player

        # Switch player
        current_player = "O" if current_player == "X" else "X"

def get_move(board, current_player):
    while True:
        try:
            row = int(input("Digite a linha: "))
            col = int(input("Digite a coluna: "))
            if not is_valid_move(board, row, col):
                raise ValueError
            break
        except ValueError:
            print("Jogada inválida, tente novamente.")

    return row, col

def is_valid_move(board, row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] is None

# Start the game
play()
