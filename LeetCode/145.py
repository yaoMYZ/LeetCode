# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.__postorder(root)

    def __postorder(self,node):
        if node==None:
            return []
        left = self.__postorder(node.left)
        right = self.__postorder(node.right)
        return left+right+[node.val]
