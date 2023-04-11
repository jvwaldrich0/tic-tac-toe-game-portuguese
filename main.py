def print_board(board):
    print("  0 1 2")
    for i in range(3):
        row = str(i) + " "
        for j in range(3):
            if board[i][j] == None:
                row += "."
            else:
                row += board[i][j]
            if j < 2:
                row += "|"
        print(row)
    print()

def is_winner(board, player):
    # Verifica se alguma das linhas está completa
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # Verifica se alguma das colunas está completa
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    # Verifica se alguma das diagonais está completa
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def is_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True

def play():
    board = [[None for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Verifica se alguém ganhou
        if is_winner(board, current_player):
            print(current_player, "venceu!")
            return

        # Verifica se é empate
        if is_tie(board):
            print("Empate!")
            return

        # Pede a jogada do jogador atual
        row = int(input("Digite a linha: "))
        col = int(input("Digite a coluna: "))

        # Verifica se a jogada é válida
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != None:
            print("Jogada inválida, tente novamente.")
        else:
            board[row][col] = current_player

            # Troca o jogador atual
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

# Inicia o jogo
play()
