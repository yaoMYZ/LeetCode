import copy
class UnionFind(object):
    """并查集类"""
    def __init__(self, n):
        """长度为n的并查集"""
        self.uf = [-1 for i in range(n + 1)]    # 列表0位置空出
        self.sets_count = n                     # 判断并查集里共有几个集合, 初始化默认互相独立

    def find(self, p):
        """尾递归"""
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        """连通p,q 让q指向p"""
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return False
        elif self.uf[proot] > self.uf[qroot]:   # 负数比较, 左边规模更小
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]  # 规模相加
            self.uf[qroot] = proot
        self.sets_count -= 1                    # 连通后集合总数减一
        return True

    def is_connected(self, p, q):
        """判断pq是否已经连通"""
        return self.find(p) == self.find(q)     # 即判断两个结点是否是属于同一个祖先

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        node_set = UnionFind(n)
        re = 0
        for e in edges:
            if e[0]==3:
                if not node_set.union(e[1],e[2]):
                    re += 1
        node_sets = [copy.deepcopy(node_set),copy.deepcopy(node_set)]
        for e in edges:
            i = e[0] - 1
            if i!=2:
                if not node_sets[i].union(e[1],e[2]):
                    re += 1
        if node_sets[0].sets_count>1 or node_sets[1].sets_count>1:
            return -1
        else:
            return re

if __name__ == '__main__':
    so = Solution()
    n = 4
    edges = [[3,2,3],[1,1,2],[2,3,4]]
    print(so.maxNumEdgesToRemove(n,edges))
