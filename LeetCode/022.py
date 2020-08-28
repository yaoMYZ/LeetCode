class Solution(object):
    def __init__(self):
        self.__ge_str_set = set()

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.__generate('(',n-1,n)
        return list(self.__ge_str_set)

    def __generate(self,ge_str,n,m):
        if n == 0:
            for i in range(m):
                ge_str += ')'
            if ge_str not in self.__ge_str_set:
                self.__ge_str_set.add(ge_str)
            return
        self.__generate(ge_str+'(',n-1,m)
        if m>n:
            self.__generate(ge_str+')',n,m-1)
        return


if __name__ == '__main__':
    so = Solution()
    print(so.generateParenthesis(3))
