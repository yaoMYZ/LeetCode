class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        key = -1
        max_num = -1
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 0
            nums_dict[n]+=1
            if nums_dict[n] > max_num:
                max_num = nums_dict[n]
                key = n
        return key

