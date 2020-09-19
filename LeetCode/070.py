class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 1
        bf1 = 0
        bf2 = 0
        for i in range(n):
            bf2 = bf1
            bf1 = r
            r = bf1 + bf2
        return r

if __name__ == '__main__':
    so = Solution()
    print(so.climbStairs(2))