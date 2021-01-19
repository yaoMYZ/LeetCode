class Solution(object):

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<2:
            return 0


        dis_point = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dis = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                dis_point.append([dis,i,j])
        dis_point = sorted(dis_point,key=lambda x:x[0])
        min_dis = 0
        edge = 0
        self.parent = []
        self.rank = []
        for i in range(len(points)):
            self.parent.append(-1)
            self.rank.append(0)
        idx = 0
        while edge<len(points)-1:
            dis = dis_point[idx][0]
            p1 = dis_point[idx][1]
            p2 = dis_point[idx][2]
            p1 = self.find(p1)
            p2 = self.find(p2)
            if p1!=p2:
                self.merge(p1,p2)
                min_dis+=dis
                edge+=1
            idx+=1
        return min_dis

    def find(self,i):
        if self.parent[i]!=-1:
            return self.find(self.parent[i])
        return i

    def merge(self,i,j):
        if self.rank[i] < self.rank[j]:
            tmp = i
            i = j
            j = tmp
        if self.rank[i]==self.rank[j]:
            self.rank[i]+=1
        self.parent[j] = i



if __name__ == '__main__':
    so = Solution()
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(so.minCostConnectPoints(points))

