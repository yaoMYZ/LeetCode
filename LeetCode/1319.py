class UnionFind(object):
    """并查集类"""
    def __init__(self, n):
        """长度为n的并查集"""
        self.uf = [-1 for i in range(n)]
        self.sets_count = n              # 判断并查集里共有几个集合, 初始化默认互相独立
        self.connect_sets = set([i for i in range(n)])

    def find(self, p):
        """尾递归"""
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        """连通p,q 让q指向p"""
        proot = p
        qroot = q
        if self.uf[proot] > self.uf[qroot]:   # 负数比较, 左边规模更小
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
            self.connect_sets.remove(proot)
        else:
            self.uf[proot] += self.uf[qroot]  # 规模相加
            self.uf[qroot] = proot
            self.connect_sets.remove(qroot)
        self.sets_count -= 1                    # 连通后集合总数减一


    def find_and_union(self,p):
        for q in self.connect_sets:
            if p!=q:
                self.union(p,q)
                break

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<n-1:
            return -1
        union = UnionFind(n)
        repeat_cons = []

        for con in connections:
            p1 = union.find(con[0])
            p2 = union.find(con[1])
            if p1!=p2:
                union.union(p1,p2)
            else:
                repeat_cons.append(con)
        if union.sets_count<=1:
            return 0
        result = 0
        for con in repeat_cons:
            p = union.find(con[0])
            union.find_and_union(p)
            result+=1
            if union.sets_count <= 1:
                break
        if union.sets_count<=1:
            return result
        else:
            return -1

if __name__ == '__main__':
    so = Solution()
    n = 12
    connections = [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]
    re = so.makeConnected(n,connections)
    print(re)
