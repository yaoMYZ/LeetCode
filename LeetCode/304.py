import copy

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.__dp = copy.deepcopy(matrix)
        self.__r = len(self.__dp)
        if self.__r<1:
            return
        self.__c = len(self.__dp[0])
        for i in range(1,self.__r):
            self.__dp[i][0] = self.__dp[i-1][0]+self.__dp[i][0]
        for i in range(1,self.__c):
            self.__dp[0][i] = self.__dp[0][i - 1] + self.__dp[0][i]

        for i in range(1,self.__r):
            for j in range(1,self.__c):
                self.__dp[i][j] = self.__dp[i-1][j]+self.__dp[i][j-1]-self.__dp[i-1][j-1]+self.__dp[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        lt = 0
        ld = 0
        rt = 0
        if row1-1>=0 and col1-1>=0:
            lt = self.__dp[row1-1][col1-1]
        if col1-1>=0:
            ld = self.__dp[row2][col1-1]
        if row1-1>=0:
            rt = self.__dp[row1-1][col2]
        return self.__dp[row2][col2]-(ld+rt-lt)

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    so = NumMatrix(matrix)
    print(so.sumRegion(2, 1, 4, 3))
    print(so.sumRegion(1, 1, 2, 2))
    print(so.sumRegion(1, 2, 2, 4))

