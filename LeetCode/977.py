class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for idx in range(len(A)):
            A[idx] = A[idx]*A[idx]
        return sorted(A)

if __name__ == '__main__':
    so = Solution()
    print(so.sortedSquares([-4,-1,0,3,10]))