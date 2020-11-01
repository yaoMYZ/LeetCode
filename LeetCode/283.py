class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                for j in range(i,len(nums)-1):
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
if __name__ == '__main__':
    so = Solution()
    nums = [0, 1, 0, 3, 12]
    so.moveZeroes(nums)
    print(nums)

