# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.__ancestor = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.__find_ancestor(root,p,q)
        return self.__ancestor

    def __find_ancestor(self, node, p, q):
        if self.__ancestor:
            return False
        if node==None:
            return False

        left = self.__find_ancestor(node.left,p,q)
        right = self.__find_ancestor(node.right,p,q)

        if self.__ancestor:
            return False

        if node==p or node==q:
            if left or right:
                self.__ancestor = node
                return False
            else:
                return True

        if left and right:
            self.__ancestor = node
            return False

        return left or right

if __name__ == '__main__':
    so = Solution()
    root = TreeNode(3)

    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right=TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(so.lowestCommonAncestor(root,root.left.right.right,root.left).val)
