class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__accus = [0]
        for i in range(len(nums)):
            self.__accus.append(self.__accus[i]+nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__accus[j+1] - self.__accus[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)