# Selecting game mode
def choose_game_mode():
    gameboard = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    print("Welcome to AI tic-tac-toe! Would you like to be X or O?")
    game = input().upper()

    if game == "X":
        print("Row is each row of the gameboard from 1-3, and column is each "
              "column of the board from 1-3")
        print_board(gameboard)
        gameplay(gameboard, True)
    elif game == "O":
        print("Row is each row of the gameboard from 1-3, and column is each "
              "column of the board from 1-3")
        gameplay(gameboard, False)


# Running game
def gameplay(gameboard, is_player_max):
    running = True
    # The maximizing player is whoever is X, so in this case, player is maximizing
    if is_player_max:
        while running:
            gameboard = player_move(gameboard, True)
            if check_winner(gameboard):
                break
            print_board(gameboard)
            gameboard = ai_move(gameboard, False)
            if check_winner(gameboard):
                break
            print_board(gameboard)
    # Computer is maximizing (player is O)
    else:
        while running:
            gameboard = ai_move(gameboard, True)
            if check_winner(gameboard):
                break
            print_board(gameboard)
            gameboard = player_move(gameboard, False)
            if check_winner(gameboard):
                break
            print_board(gameboard)


# Checks winner - returns True if there is a winner, false if not
def check_winner(gameboard):
    result = winning_condition(gameboard)
    if result != " ":
        if result != "tie":
            print(winning_condition(gameboard) + " wins!")
        else:
            print("It's a tie!")
        print_board(gameboard)
        return True
    else:
        return False


# Prints gameboard
def print_board(gameboard):
    for i in range(3):
        print(gameboard[i][0] + '|' + gameboard[i][1] + '|' + gameboard[i][2])
        if i < 2:
            print('-+-+-')


def player_move(gameboard, is_player_max):
    invalid_move = True
    if is_player_max:
        player = "X"
    else:
        player = "O"
    print("Where would you like to go?")
    # Loops until valid move is selected
    while invalid_move:
        row = int(input("Row ")) - 1
        column = int(input("Column ")) - 1

        if gameboard[row][column] == " ":
            gameboard[row][column] = player
            return gameboard
        else:
            print("Sorry, that spot is full. Where would you like to go?")


# Makes best possible move for computer based on Minimax algorithm
def ai_move(gameboard, is_ai_max):
    if is_ai_max:
        ai = "X"
        best_score = float('-inf')
        move = [0, 0]
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] == " ":
                    gameboard[i][j] = ai
                    score = minimax(gameboard, 8, float('-inf'), float('inf'), False, ai)
                    gameboard[i][j] = " "
                    if score > best_score:
                        best_score = score
                        move[0] = i
                        move[1] = j

        gameboard[move[0]][move[1]] = ai
        return gameboard
    else:
        ai = "O"
        best_score = float('inf')
        move = [0, 0]
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] == " ":
                    gameboard[i][j] = ai
                    score = minimax(gameboard, 8, float('inf'), float('-inf'), True, ai)
                    gameboard[i][j] = " "
                    if score < best_score:
                        best_score = score
                        move[0] = i
                        move[1] = j

        gameboard[move[0]][move[1]] = ai
        return gameboard


def winning_condition(gameboard):
    winner = " "

    # checking row
    for row in range(3):
        if gameboard[row][0] == gameboard[row][1] == gameboard[row][2] != " ":
            winner = gameboard[row][2]

    # checking column
    for column in range(3):
        if gameboard[0][column] == gameboard[1][column] == gameboard[2][column] != " ":
            winner = gameboard[2][column]

    # checking diagonal
    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != " ":
        winner = gameboard[2][2]

    if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] != " ":
        winner = gameboard[2][0]

    # check for tie
    openspots = 0
    for i in range(3):
        for j in range(3):
            if gameboard[i][j] == " ":
                openspots = openspots + 1

    if openspots == 0 and winner == " ":
        return "tie"
    else:
        return winner


# Implementation of the minimax algorithm
def minimax(gameboard, depth, alpha, beta, is_max, ai_value):
    scores = {"X": 10, "O": -10, "tie": 0}

    result = winning_condition(gameboard)
    if result != " " or depth == 0:
        return scores[result]

    if ai_value == "X":
        ai = "X"
        player = "O"
    else:
        ai = "O"
        player = "X"

    if is_max:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] == " ":
                    gameboard[i][j] = player
                    score = minimax(gameboard, depth - 1, alpha, beta, False, ai_value)
                    gameboard[i][j] = " "
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if gameboard[i][j] == " ":
                    gameboard[i][j] = ai
                    score = minimax(gameboard, depth - 1, alpha, beta, True, ai_value)
                    gameboard[i][j] = " "
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if alpha >= beta:
                        break
        return best_score


def main():
    playing = True
    while playing:
        choose_game_mode()
        print("Play again? Y/N")
        ans = input().upper()
        if ans == "N":
            break


if __name__ == "__main__":
    main()
