class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        Ai = 0
        for a in A:
            Ai*=10
            Ai += a
        re = Ai+K
        if re==0:
            return [0]
        res = []
        while re>0:
            res.append(re%10)
            re=int(re/10)
        return res[::-1]

if __name__ == '__main__':
    so = Solution()
    A= [0]
    K = 0
    print(so.addToArrayForm(A,K))
