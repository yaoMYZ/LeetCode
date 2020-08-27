import heapq
import collections

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(curr):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        stack.reverse()
        # stack = stack[::-1]# [::-1]反转数组
        return stack

if __name__ == '__main__':
    j = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    solu = Solution()
    print(solu.findItinerary(j))