class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        re = 0
        for idx in range(0,len(nums),2):
            re+=nums[idx]
        return re

if __name__ == '__main__':
    so = Solution()
    nums = [6,2,6,5,1,2]
    print(so.arrayPairSum(nums))
