import numpy

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        point = numpy.asarray([0,0])
        move_dict = {'R':numpy.asarray([0,1]),'L':numpy.asarray([0,-1]),
                     'U':numpy.asarray([-1,0]),'D':numpy.asarray([1,0])}
        for move in moves:
            point += move_dict[move]
        if point[0]==0 and point[1]==0:
            return True
        return False

if __name__ == '__main__':
    solu = Solution()
    print(solu.judgeCircle("LL"))
