import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def is_draw():
    return " " not in board

def play_game():
    print("Tic Tac Toe Game: You (X) vs AI (O)")

    while True:
        print_board()
        try:
            move = int(input("Choose position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position!")
                continue
        except:
            print("Please enter a number between 1 and 9")
            continue

        if board[move] == " ":
            board[move] = "X"
        else:
            print("Position already taken!")
            continue

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        ai_move = random.choice([i for i in range(9) if board[i] == " "])
        board[ai_move] = "O"

        if check_winner("O"):
            print_board()
            print("🤖 AI wins!")
            break

play_game()
