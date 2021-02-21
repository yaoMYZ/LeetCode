from sortedcontainers import SortedList

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        si, ei = 0, 0
        re = 0
        snums = SortedList()
        while ei<len(nums):
            snums.add(nums[ei])
            while abs(snums[0]-snums[-1])>limit:
                snums.remove(nums[si])
                si+=1
            re = max(re,ei-si+1)
            ei += 1
        return re

if __name__ == '__main__':
    so = Solution()
    nums = [8,2,4,7]
    limit = 4
    print(so.longestSubarray(nums,limit))


