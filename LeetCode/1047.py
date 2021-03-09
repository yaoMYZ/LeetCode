class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        tmp = []
        for ts in S:
            if len(tmp)>0 and tmp[-1]==ts:
                tmp.pop(-1)
            else:
                tmp.append(ts)
        re = ''.join(tmp)
        return re

if __name__ == '__main__':
    so = Solution()
    S = "abbaca"
    print(so.removeDuplicates(S))