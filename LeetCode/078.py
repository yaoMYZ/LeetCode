import copy

class Solution(object):
    def __init__(self):
        self.__result = []
        pass

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.__subsets(nums,0,[])
        return self.__result

    def __subsets(self,nums,idx,tmp_nums):
        self.__result.append(copy.deepcopy(tmp_nums))
        for i in range(idx,len(nums)):
            tmp_nums.append(nums[i])
            self.__subsets(nums,i+1,tmp_nums)
            tmp_nums.pop()

if __name__ == '__main__':
    so = Solution()
    print(so.subsets([1,2,3]))