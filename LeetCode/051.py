class Solution(object):
    def __init__(self):
        self.__all_solution = []
        self.__direction = [[-1,1],[1,1],[1,-1],[-1,-1]]
        pass

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        mat = self.__init_mat(n)
        col_set = set()
        for i in range(n):
            mat[n-1][i] = 'Q'
            col_set.add(i)
            self.__sub__solve(mat,n-2,col_set)
            col_set.remove(i)
            mat[n - 1][i] = '.'
        return self.__all_solution

    def __init_mat(self,n):
        mat = []
        for i in range(n):
            mat.append([])
            for j in range(n):
                mat[i].append('.')
        return mat

    def __sub__solve(self,mat,last,col_set):
        if last==-1:
            self.__all_solution.append(self.__get_str_mat(mat))
            return
        n = len(mat)
        for i in range(n):
            if i in col_set:
                continue
            set_flag = True
            for dir in self.__direction:
                if not set_flag:
                    break
                for j in range(1,n):
                    row = dir[0]*j+last
                    col = dir[1]*j+i
                    if self.__if_in_bound(row,n) and self.__if_in_bound(col,n):
                        if mat[row][col]=='Q':
                            set_flag=False
                            break
                    else:
                        break
            if set_flag:
                mat[last][i] = 'Q'
                col_set.add(i)
                self.__sub__solve(mat,last-1,col_set)
                col_set.remove(i)
                mat[last][i] = '.'

    def __if_in_bound(self,idx,n):
        if idx>=0 and idx<n:
            return True
        else:
            return False

    def __get_str_mat(self,mat):
        str_mat = []
        for row in mat:
            tmp_str=''
            for i in row:
                tmp_str+=i
            str_mat.append(tmp_str)
        return str_mat


if __name__ == '__main__':
    so = Solution()
    arr = so.solveNQueens(4)
    for a in arr:
        print(a)