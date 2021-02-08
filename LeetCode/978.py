class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr)<2:
            return 1
        re = 1
        cur_re = 1
        dif = arr[0]-arr[1]
        if dif!=0:
            cur_re+=1
            re+=1
        for k in range(1,len(arr)-1):
            tmp_dif = arr[k]-arr[k+1]
            if dif*tmp_dif<0:
                cur_re+=1
                re = max(re,cur_re)
            else:
                cur_re = 1
                if tmp_dif!=0:
                    cur_re+=1
            dif = tmp_dif
        return re

if __name__ == '__main__':
    so = Solution()
    arr = [4,8,12,16]
    print(so.maxTurbulenceSize(arr))