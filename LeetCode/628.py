class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        re = nums[-1]*nums[-2]*nums[-3]
        if nums[1]<0:
            return max(nums[0]*nums[1]*nums[-1],re)
        return re

if __name__ == '__main__':
    so = Solution()
    nums = [-100,-1,1,2,3,4]
    r = so.maximumProduct(nums)
    print(r)