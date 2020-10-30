class Solution(object):
    def __init__(self):
        self.__perimeter = 0
        self.__direction = [[1,0],[-1,0],[0,-1],[0,1]]

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        self.__flags = [[True for i in range(len(grid[0]))] for j in range(len(grid))]
        r,c=0,0
        len_r,len_c = len(grid),len(grid[0])
        while grid[r][c]!=1 and r<len_r:
            c+=1
            if c==len_c:
                r+=1
                c=0
        self.__get_perimeter(grid,[r,c])
        return self.__perimeter

    def __get_perimeter(self,grid,pos):
        if not self.__flags[pos[0]][pos[1]]:
            return
        self.__flags[pos[0]][pos[1]] = False
        for dir in self.__direction:
            r = pos[0]+dir[0]
            c = pos[1]+dir[1]
            if len(grid)>r>=0 and len(grid[0])>c>=0:
                if grid[r][c]==1:
                    self.__get_perimeter(grid,[r,c])
                else:
                    self.__perimeter+=1
            else:
                self.__perimeter+=1

if __name__ == '__main__':
    so = Solution()
    grid = [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]]
    print(so.islandPerimeter(grid))