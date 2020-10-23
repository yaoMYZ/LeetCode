class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__nums = []
        self.__min = 10e10


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.__nums.append(x)
        if x<self.__min:
            self.__min = x

    def pop(self):
        """
        :rtype: None
        """
        self.__nums.pop(-1)
        if len(self.__nums)==0:
            self.__min = 10e10
        else:
            self.__min = min(self.__nums)


    def top(self):
        """
        :rtype: int
        """
        return self.__nums[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.__min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()