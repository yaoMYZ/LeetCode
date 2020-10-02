class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_set = set()
        for j in J:
            j_set.add(j)
        num=0
        for s in S:
            if s in j_set:
                num+=1
        return num


if __name__ == '__main__':
    so = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(so.numJewelsInStones(J,S))