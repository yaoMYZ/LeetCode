import bisect

class Solution:
    def countRangeSum(self, nums, lower, upper):
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            right = bisect.bisect_right(pre, now - lower)
            left = bisect.bisect_left(pre, now - upper)
            res += right - left
            bisect.insort(pre, now)
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(so.countRangeSum(nums,lower,upper))