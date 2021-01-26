class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dim_set = {}
        re = 0
        for d in dominoes:
            tmp = sorted(d)
            tmp = tuple(tmp)
            if tmp in dim_set:
                dim_set[tmp]+=1
            else:
                dim_set[tmp]=1
        for val in dim_set.values():
            re+=int(val*(val-1)/2)
        return re


if __name__ == '__main__':
    so = Solution()
    dominoes=[[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]
    r = so.numEquivDominoPairs(dominoes)
    print(r)