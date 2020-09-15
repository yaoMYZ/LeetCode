# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.__traversal(root)

    def __traversal(self,node):
        if node==None:
            return []
        left_nodes = self.__traversal(node.left)
        right_nodes = self.__traversal(node.right)
        return left_nodes+[node.val]+right_nodes

