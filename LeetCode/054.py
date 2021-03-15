class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = len(matrix)
        c = len(matrix[0])
        flag = [[True]*c for i in range(r)]
        pos = [[0,1],[1,0],[0,-1],[-1,0]]
        pi = 0
        cpos = [0,-1]
        res = []
        while len(res)<r*c:
            tpos = [cpos[0] + pos[pi][0], cpos[1] + pos[pi][1]]
            if tpos[0]>=0 and tpos[0]<r and tpos[1]>=0 and tpos[1]<c and flag[tpos[0]][tpos[1]]:
                cpos = tpos
            else:
                pi = (pi+1)%4
                cpos = [cpos[0] + pos[pi][0], cpos[1] + pos[pi][1]]
            res.append(matrix[cpos[0]][cpos[1]])
            flag[cpos[0]][cpos[1]] = False
        return res

if __name__ == '__main__':
    so = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(so.spiralOrder(matrix))