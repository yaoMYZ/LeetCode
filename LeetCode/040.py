import copy
class Solution(object):
    def __init__(self):
        self.__result = set()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.__subCombine(candidates,0,target,[])
        return list(self.__result)

    def __subCombine(self, candidates, idx, target, nums):
        if target<0:
            return
        if target==0:
            tmp=copy.deepcopy(nums)
            tmp = tuple(sorted(tmp))
            if tmp not in self.__result:
                self.__result.add(tmp)
        if idx >= len(candidates):
            return
        self.__subCombine(candidates,idx+1,target,nums)
        nums.append(candidates[idx])
        self.__subCombine(candidates,idx+1,target-candidates[idx],nums)
        nums.pop()

if __name__ == '__main__':
    so = Solution()
    nums = [10,1,2,7,6,1,5]
    target = 8
    print(so.combinationSum2(nums,target))