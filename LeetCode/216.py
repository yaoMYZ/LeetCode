import copy
class Solution(object):
    def __init__(self):
        self.__result = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = range(1,10)
        self.__subCombine(candidates,0,n,k,[])
        return list(self.__result)

    def __subCombine(self, candidates, idx, target,k,nums):
        if target<0:
            return
        if len(nums)==k:
            if target==0:
                tmp=copy.deepcopy(nums)
                self.__result.append(tmp)
            return
        if idx >= len(candidates):
            return
        self.__subCombine(candidates,idx+1,target,k,nums)
        nums.append(candidates[idx])
        self.__subCombine(candidates,idx+1,target-candidates[idx],k,nums)
        nums.pop()

if __name__ == '__main__':
    so = Solution()
    print(so.combinationSum3(3,9))