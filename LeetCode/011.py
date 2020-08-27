class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        r = len(height)-1
        l = 0
        while(r>l):
            max_area = max(max_area,min(height[l],height[r])*(r-l))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1

        return max_area

if __name__ == '__main__':
    arr = [1,8,6,2,5,4,8,3,7]
    solu = Solution()
    print(solu.maxArea(arr))
