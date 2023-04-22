class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num: int, row: int, col: int) -> bool:
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            row0, col0 = (row // 3) * 3, (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[row0 + i][col0 + j] == num:
                        return False
            return True

        def backtrack(row: int, col: int) -> bool:
            if row == 9:
                return True
            if col == 9:
                return backtrack(row + 1, 0)
            if board[row][col] != '.':
                return backtrack(row, col + 1)
            for num in range(1, 10):
                if is_valid(str(num), row, col):
                    board[row][col] = str(num)
                    if backtrack(row, col + 1):
                        return True
                    board[row][col] = '.'
            return False

        backtrack(0, 0)
