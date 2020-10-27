# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.__traversal(root)

    def __traversal(self,node):
        if node==None:
            return []
        l_list = self.__traversal(node.left)
        r_list = self.__traversal(node.right)
        return [node.val]+l_list+r_list