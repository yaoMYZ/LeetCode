import numpy as np
class Solution(object):
    def __init__(self):
        self.__if_visit_all = False
        pass

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.__rooms = rooms
        visit_arr = np.zeros(len(rooms))
        self.__subVisit(0,visit_arr)
        return self.__if_visit_all

    def __subVisit(self,ri,visit_arr):
        if self.__if_visit_all:
            return
        visit_arr[ri] = 1

        to_rooms = self.__rooms[ri]
        if_visit = False
        for room in to_rooms:
            if visit_arr[room]==0:
                self.__subVisit(room,visit_arr)
                if_visit = True
        if not if_visit and sum(visit_arr)==len(self.__rooms):
            self.__if_visit_all = True

if __name__ == '__main__':
    so = Solution()
    lis = [[1,3],[3,0,1],[2],[0]]
    print(so.canVisitAllRooms(lis))


