import numpy as np

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0

        one_num = 0
        max_area = 0
        mat = np.zeros([len(matrix),len(matrix[0])])
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                mat[i, 0] = 1
                one_num += 1

        for i in range(1,len(matrix[0])):
            if matrix[0][i]=='1':
                mat[0,i] = mat[0,i-1]+1
                one_num+=1

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '1':
                    mat[i, j] = mat[i, j - 1] + 1
                    one_num += 1
                for k in range(i-1,-1,-1):
                    height = i-k+1
                    width = min(mat[k:i+1,j])
                    if height>width:
                        break
                    else:
                        max_area = max(max_area,height*height)
        if max_area==0:
            return 1 if one_num>0 else 0

        return max_area

if __name__ == '__main__':
    so = Solution()
    matrix = [
        "10100",
        "10111",
        "11111",
        "10010"
    ]
    print(so.maximalSquare(matrix))