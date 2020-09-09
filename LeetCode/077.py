import copy
class Solution(object):
    def __init__(self):
        self.__result = []
        self.__flags = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.__flags = [True for i in range(n)]
        self.__subCombine(k,[])
        return self.__result

    def __subCombine(self,k,nums):
        if k==0:
            self.__result.append(copy.deepcopy(nums))
            return
        k-=1
        flags_set = []
        for i in range(len(self.__flags)):
            if self.__flags[i]:
                self.__flags[i]=False
                flags_set.append(i)
                nums.append(i + 1)
                self.__subCombine(k,nums)
                nums.pop()
        for idx in flags_set:
            self.__flags[idx] = True

if __name__ == '__main__':
    so = Solution()
    print(so.combine(4,2))

