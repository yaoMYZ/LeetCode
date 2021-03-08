class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        record = [[False]*n for i in range(n)]
        for i in range(n):
            record[i][i] = True
        for c in range(1,n):
            for r in range(c):
                if r+1>=c-1 or record[r+1][c-1]:
                    if s[r]==s[c]:
                        record[r][c]=True
        f = [n]*n
        for i in range(n):
            if record[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if record[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
        return f[n-1]


if __name__ == '__main__':
    so = Solution()
    s = "aab"
    print(so.minCut(s))
