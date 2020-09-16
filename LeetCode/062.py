import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

if __name__ == '__main__':
    so = Solution()
    print(so.uniquePaths(7,3))
