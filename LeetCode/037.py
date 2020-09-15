class Solution(object):
    def __init__(self):
        self.line = [[False] * 9 for _ in range(9)]
        self.column = [[False] * 9 for _ in range(9)]
        self.block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        self.valid = False
        self.spaces = list()

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    self.spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = True

        self.dfs(0,board)

    def dfs(self,pos,board):
        if pos == len(self.spaces):
            self.valid = True
            return

        i, j = self.spaces[pos]
        for digit in range(9):
            if self.line[i][digit] == self.column[j][digit] == self.block[i // 3][j // 3][digit] == False:
                self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = True
                board[i][j] = str(digit + 1)
                self.dfs(pos + 1,board)
                self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = False
            if self.valid:
                return