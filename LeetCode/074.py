class Solution(object):
    def binarySearch(self,num,target,sidx,eidx):
        if sidx>eidx:
            return False
        mid = (int)((eidx-sidx)/2+sidx)
        if num[mid]==target:
            return True
        if num[mid]>target:
            return self.binarySearch(num,target,sidx,mid-1)
        else:
            return self.binarySearch(num,target,mid+1,eidx)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        sbound = -100000
        for i in range(row):
            if target>sbound and target<=matrix[i][-1]:
                return self.binarySearch(matrix[i],target,0,col-1)
            sbound = matrix[i][-1]
        return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 6
    so = Solution()
    print(so.searchMatrix(matrix,target))