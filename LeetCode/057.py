class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new_list = []
        ni = newInterval
        for i in range(len(intervals)):
            if intervals[i][1]<ni[0]:
                new_list.append(intervals[i])
            else:
                if intervals[i][0]>ni[1]:
                    new_list.append(ni)
                    new_list += intervals[i:]
                    return new_list
                else:
                    s_idx = min(intervals[i][0],ni[0])
                    for j in range(i,len(intervals)):
                        if intervals[j][0]>ni[1]:
                            e_idx = ni[1]
                            new_list.append([s_idx,e_idx])
                            new_list += intervals[j:]
                            return new_list
                        elif intervals[j][1]<ni[1]:
                            continue
                        else:
                            e_idx = intervals[j][1]
                            new_list.append([s_idx,e_idx])
                            if j+1<len(intervals):
                                new_list += intervals[j+1:]
                            return new_list
                    e_idx = ni[1]
                    new_list.append([s_idx,e_idx])
                    return new_list
        new_list.append(newInterval)
        return new_list

if __name__ == '__main__':
    so = Solution()
    intervals = [[1,5]]
    newInterval = [2,7]
    print(so.insert(intervals,newInterval))