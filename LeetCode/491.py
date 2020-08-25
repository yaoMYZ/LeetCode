class Solution(object):
    def __init__(self):
        self.__nums_len = 0

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.__nums_len = len(nums)
        subSeqs = self.__subFindSubsequences(nums)
        result = set()
        for subSeq in subSeqs:
            if len(subSeq)>=2 and tuple(subSeq) not in result:
                result.add(tuple(subSeq))
        return list(result)

    def __subFindSubsequences(self,nums):
        if len(nums)==0:
            return []
        subSeqs = [[nums[0]],[]]
        for num in nums[1:]:
            len_s = len(subSeqs)
            for i in range(len_s):
                if len(subSeqs[i])==0:
                    subSeqs.append([num])
                elif subSeqs[i][-1]<=num:
                    tmp = subSeqs[i] + [num]
                    subSeqs.append(tmp)
        return subSeqs


if __name__ == '__main__':
    arr = [4,6,8]
    solution = Solution()
    nums = solution.findSubsequences(arr)
    print(nums)