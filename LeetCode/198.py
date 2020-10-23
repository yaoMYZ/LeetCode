class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        record = [0]*len(nums)
        record[0] = nums[0]
        record[1] = nums[1]
        record[2] = nums[0]+nums[2]
        for i in range(3,len(nums)):
            record[i] = max(record[i-2],record[i-3])+nums[i]
        return max(record[-1],record[-2])


if __name__ == '__main__':
    so = Solution()
    print(so.rob([1,2,3,1]))