class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_idx = 0
        for idx in range(len(nums)):
            if max_idx>=len(nums)-1:
                return True
            if max_idx<idx:
                return False
            max_idx = max(max_idx,idx+nums[idx])

        return max_idx>=len(nums)-1


if __name__ == '__main__':
    so = Solution()
    nums = [3,2,1,0,4]
    print(so.canJump(nums))