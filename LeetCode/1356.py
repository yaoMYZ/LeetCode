class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        new_arr = []
        for i in range(len(arr)):
            n = arr[i]
            new_arr.append([self.__count_num(n),n,i])
        arr = sorted(new_arr)
        arr = [n[1] for n in arr]
        return arr

    def __count_num(self,n):
        count = 0
        while n!=0:
            count += n&1
            n = n>>1
        return count

if __name__ == '__main__':
    so = Solution()
    arr = [10000,10000]
    print(so.sortByBits(arr))