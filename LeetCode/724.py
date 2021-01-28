class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return -1
        left = 0
        right = sum(nums[1:])
        if left==right:
            return 0
        for i in range(1,len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left==right:
                return i
        return -1

if __name__ == '__main__':
    so = Solution()
    nums = [0,0,1]
    print(so.pivotIndex(nums))
