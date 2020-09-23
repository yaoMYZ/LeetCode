# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root):
        def dfs(root):
            if not root:
                return [float("inf"), 0, 0]

            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]

        a, b, c = dfs(root)
        return b


if __name__ == '__main__':
    so = Solution()
    # root = TreeNode(0)
    # root.left = TreeNode(0)
    # root.left.left = TreeNode(0)
    # root.left.right = TreeNode(0)
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.left.left = TreeNode(0)
    root.left.left.left.right = TreeNode(0)
    root.left.left.left.right.left = TreeNode(0)
    print(so.minCameraCover(root))
