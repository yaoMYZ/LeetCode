import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.__edges = collections.defaultdict(list)
        self.__visited = [0] * numCourses
        self.__result = list()
        self.__valid = True
        for info in prerequisites:
            self.__edges[info[1]].append(info[0])

        for i in range(numCourses):
            if self.__valid and not self.__visited[i]:
                self.__dfs(i)

        return self.__valid

    def __dfs(self,u):
        self.__visited[u] = 1
        for v in self.__edges[u]:
            if self.__visited[v] == 0:
                self.__dfs(v)
                if not self.__valid:
                    return
            elif self.__visited[v] == 1:
                self.__valid = False
                return
        self.__visited[u] = 2
        self.__result.append(u)


if __name__ == '__main__':
    so = Solution()
    print(so.canFinish(2, [[1,0],[0,1]]))
