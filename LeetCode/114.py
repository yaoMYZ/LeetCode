# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left==None:
            return
        tmp_node = root.right
        root.right = root.left
        left = root.left
        while left.right!=None:
            left = left.right
        left.right = tmp_node
        root.left = None

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    so = Solution()
    so.flatten(root)
    print(root)