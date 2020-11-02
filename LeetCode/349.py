class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_set = set()
        result = set()
        for n in nums1:
            num_set.add(n)
        for n in nums2:
            if n in num_set:
                result.add(n)
        return list(result)

