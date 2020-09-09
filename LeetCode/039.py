import copy
class Solution(object):
    def __init__(self):
        self.__result = set()
        pass

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.__sub_combine(candidates,target,[])
        return list(self.__result)

    def __sub_combine(self,candidates, target, nums):
        if target<0:
            return
        if target==0:
            tmp = copy.deepcopy(nums)
            tmp = tuple(sorted(tmp))
            if tmp not in self.__result:
                self.__result.add(tmp)
            return
        for can in candidates:
            nums.append(can)
            self.__sub_combine(candidates,target-can,nums)
            nums.pop()

if __name__ == '__main__':
    so = Solution()
    print(so.combinationSum([2,3,6,7],7))