# class Solution:
#     def videoStitching(self, clips,T):
#         dp = [0] + [float("inf")] * T
#         for i in range(1, T + 1):
#             for aj, bj in clips:
#                 if aj < i <= bj:
#                     dp[i] = min(dp[i], dp[aj] + 1)
#
#         return -1 if dp[T] == float("inf") else dp[T]

class Solution:
    def videoStitching(self, clips, T):
        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)

        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last

        return ret



if __name__ == '__main__':
    so = Solution()
    clips = [[0,4],[2,8]]
    T = 5
    print(so.videoStitching(clips,T))