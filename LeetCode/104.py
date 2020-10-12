# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.__get_depth(root)

    def __get_depth(self,node):
        if node==None:
            return 0
        return max(self.__get_depth(node.right),self.__get_depth(node.left))+1