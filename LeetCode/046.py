import copy
class Solution(object):
    def __init__(self):
        self.__result = []
        self.__flags = []
        self.__nums = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.__flags = [True for n in nums]
        self.__subPermute(nums)
        return self.__result

    def __subPermute(self,nums):
        if len(self.__nums)==len(nums):
            tmp = copy.deepcopy(self.__nums)
            self.__result.append(tmp)
            return
        for i in range(len(nums)):
            if self.__flags[i]:
                self.__flags[i]=False
                self.__nums.append(nums[i])
                self.__subPermute(nums)
                self.__nums.pop()
                self.__flags[i]=True


if __name__ == '__main__':
    so = Solution()
    print(so.permute([1,2,3]))