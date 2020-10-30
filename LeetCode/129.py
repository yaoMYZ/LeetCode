# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.__sum_num = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        self.__sum(root,0)
        return self.__sum_num

    def __sum(self,node,sum):
        if node==None:
            return
        sum = sum*10+node.val
        if node.left==None and node.right==None:
            self.__sum_num += sum

        self.__sum(node.left,sum)
        self.__sum(node.right,sum)