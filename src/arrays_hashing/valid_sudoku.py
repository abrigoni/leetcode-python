from typing import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key of (r/3,c/3) integer division

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                if (
                    value in rows[r] or
                    value in cols[c] or
                    value in squares[(r//3,c//3)]
                ):
                    return False
                rows[r].add(value)
                cols[c].add(value)
                squares[(r//3, c//3)].add(value)
        return True

if __name__ == '__main__':
    sol = Solution()
    sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])