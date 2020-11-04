class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        record = [1 for n in nums]
        max_len = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    record[i] = max(record[i],record[j]+1)
            max_len = max(max_len,record[i])
        return max_len

if __name__ == '__main__':
    so = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(so.lengthOfLIS(nums))