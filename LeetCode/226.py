# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.__subInvert(root)
        return root

    def __subInvert(self,node):
        if node==None:
            return
        tmp = node.left
        node.left = node.right
        node.right = tmp

        self.__subInvert(node.right)
        self.__subInvert(node.left)
