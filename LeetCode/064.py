import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.row = len(grid)
        self.col = len(grid[0])
        sum_mat = np.zeros((self.row,self.col),dtype=np.int)
        sum_mat[0,0]=grid[0][0]
        for i in range(1,self.col):
            sum_mat[0,i] = sum_mat[0,i-1]+grid[0][i]
        for i in range(1, self.row):
            sum_mat[i, 0] = sum_mat[i-1, 0] + grid[i][0]

        for i in range(1,self.row):
            for j in range(1,self.col):
                sum_mat[i,j] = min(sum_mat[i-1,j],sum_mat[i,j-1])+grid[i][j]
        return sum_mat[-1,-1]


if __name__ == '__main__':
    so = Solution()
    nums = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(so.minPathSum([[0]]))
