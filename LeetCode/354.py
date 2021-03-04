
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n<=0:
            return 0
        arr = sorted(envelopes,key=lambda x:(x[0],-x[1]))
        f = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[j][1] < arr[i][1]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)

if __name__ == '__main__':
    so = Solution()
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print(so.maxEnvelopes(envelopes))
