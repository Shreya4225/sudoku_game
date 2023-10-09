def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


def is_valid_move(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    subgrid_row, subgrid_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[subgrid_row + i][subgrid_col + j] == num:
                return False

    return True


def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

#backtracking function
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def main():
    # Initialize an empty Sudoku board (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Welcome to Sudoku!")

    while not is_board_full(board):
        print_board(board)
        try:
            row = int(input("Enter row (1-9): ")) - 1
            col = int(input("Enter column (1-9): ")) - 1
            num = int(input("Enter a number (1-9): "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
            if board[row][col] == 0 and is_valid_move(board, row, col, num):
                board[row][col] = num
            else:
                print("Invalid move. Please try again.")
        else:
            print("Invalid input. Please enter valid numbers.")

    if solve_sudoku(board):
        print("Congratulations! You solved the Sudoku puzzle.")
        print_board(board)
    else:
        print("No solution exists for this puzzle.")


if __name__ == "__main__":
    main()
