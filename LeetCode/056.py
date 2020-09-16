class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==0:
            return []
        intervals = sorted(intervals,key=lambda x: x[0])
        result = [intervals[0]]
        for inter in intervals[1:]:
            if result[-1][1]>=inter[0]:
                result[-1][1]=max(result[-1][1],inter[1])
            else:
                result.append(inter)
        return result

if __name__ == '__main__':
    so = Solution()
    nums= [[1,4],[0,4]]
    print(so.merge(nums))
