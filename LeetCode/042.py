
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        flags = [True for h in height]
        s_nums = [[height[i],i] for i in range(len(height))]
        s_nums = sorted(s_nums)
        h_idx = len(height)-1
        flags[s_nums[h_idx][1]]=False
        scan_num = 1
        area = 0
        while scan_num<len(height):
            h_idx = self.__find_height_idx(h_idx,flags,s_nums)
            s_h_idx = self.__find_second_height_idx(h_idx,flags,s_nums)
            scan_num+=1
            flags[s_nums[s_h_idx][1]]=False

            idx1 = s_nums[h_idx][1]
            idx2 = s_nums[s_h_idx][1]
            area += (abs(idx2-idx1)-1)*s_nums[s_h_idx][0]
            if idx1<idx2:
                for idx in range(idx1+1,idx2):
                    if flags[idx]:
                        flags[idx]=False
                        scan_num += 1
                    area-=height[idx]

            else:
                for idx in range(idx2+1,idx1):
                    if flags[idx]:
                        flags[idx]=False
                        scan_num += 1
                    area-=height[idx]
        return area

    def __find_height_idx(self,h_idx,flags,s_nums):
        tmp_idx = s_nums[h_idx][1]
        while (tmp_idx - 1 < 0 or flags[tmp_idx - 1] == False) and (
                tmp_idx + 1 >= len(flags) or flags[tmp_idx + 1] == False):
            h_idx -= 1
            tmp_idx = s_nums[h_idx][1]
        return h_idx

    def __find_second_height_idx(self,h_idx,flags,s_nums):
        s_h_idx = h_idx - 1
        if s_nums[h_idx][1]-1>=0 and flags[s_nums[h_idx][1]-1]==True:
            while not flags[s_nums[s_h_idx][1]] or s_nums[h_idx][1]<s_nums[s_h_idx][1]:
                s_h_idx-=1
        else:
            while not flags[s_nums[s_h_idx][1]] or s_nums[h_idx][1]>s_nums[s_h_idx][1]:
                s_h_idx-=1
        return s_h_idx

if __name__ == '__main__':
    height = [1]
    so = Solution()
    print(so.trap(height))