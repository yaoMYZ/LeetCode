import math

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        sorted_arr = []
        for i in range(len(points)):
            p = points[i]
            dis = math.sqrt(p[0]*p[0]+p[1]*p[1])
            sorted_arr.append([dis,i])
        sorted_arr = sorted(sorted_arr)
        return [points[data[1]] for data in sorted_arr[:K]]

if __name__ == '__main__':
    so = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    print(so.kClosest(points,K))

