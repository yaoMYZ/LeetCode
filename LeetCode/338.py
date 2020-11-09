class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        self.record = [0]*(num+1)
        for n in range(num,0,-1):
            self.__get_num(n)
        return self.record

    def __get_num(self,n):
        if n==0:
            return
        if self.record[n]!=0:
            return
        self.__get_num(n // 2)
        self.record[n] = self.record[n//2]+n%2

if __name__ == '__main__':
    so = Solution()
    print(so.countBits(5))