# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0
        pass

    def convertBST(self, root):
        self.dfs(root)
        return root

    def dfs(self,root):
        if root:
            self.dfs(root.right)
            self.total += root.val
            root.val = self.total
            self.dfs(root.left)

if __name__ == '__main__':
    so = Solution()
    root = TreeNode(2)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-4)
    root.left.right = TreeNode(1)
    so.convertBST(root)
    print('done')