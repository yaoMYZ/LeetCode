class Solution(object):
    def __init__(self):
        self.__find = False
        self.__direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        pass

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.__row = len(board)
        self.__col = len(board[0])
        self.__flags = [[True for i in range(self.__col)] for j in range(self.__row)]
        for r in range(self.__row):
            for c in range(self.__col):
                if board[r][c] == word[0]:
                    self.__flags[r][c] = False
                    self.__subFind(board, r, c, 1, word)
                    self.__flags[r][c] = True
        return self.__find

    def __subFind(self, board, p_r, p_c, idx, word):
        if self.__find:
            return
        if idx >= len(word):
            self.__find = True
            return

        for direc in self.__direction:
            n_r = direc[0] + p_r
            n_c = direc[1] + p_c
            if n_r >= 0 and n_r < self.__row and n_c >= 0 and n_c < self.__col:
                if board[n_r][n_c] == word[idx] and self.__flags[n_r][n_c]:
                    self.__flags[n_r][n_c]=False
                    self.__subFind(board, n_r, n_c, idx + 1, word)
                    self.__flags[n_r][n_c]=True


if __name__ == '__main__':
    so = Solution()
    board = [["a","a"]]
    word = "aaa"
    print(so.exist(board,word))
