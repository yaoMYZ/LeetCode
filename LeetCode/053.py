class Solution:
    def maxSubArray(self, nums):
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            tmp = dp[i-1]+nums[i]
            dp[i]= max(tmp,nums[i])
        return max(dp)
