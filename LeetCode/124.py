# Definition for a binary tree node.
import numpy as np

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.__max_val = -10e10

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum1,sum2=self.__sum(root)
        if sum2==0 and sum1<0:
            return self.__max_val
        else:
            return max(sum1,sum2,self.__max_val)

    def __sum(self,node):
        if node==None:
            return 0,0
        self.__max_val = max(self.__max_val,node.val)
        lsum1,lsum2 = self.__sum(node.left)
        rsum1,rsum2 = self.__sum(node.right)
        return max(max(lsum1,rsum1)+node.val,node.val),np.max([lsum1,lsum2,rsum1,rsum2,node.val+lsum1+rsum1])

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(-1)
    root.right = TreeNode(-2)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    so = Solution()
    print(so.maxPathSum(root))