import functools

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.__dp(root,True)

    @functools.lru_cache(None)
    def __dp(self,node,rob_flag):
        if node==None:
            return 0
        if not rob_flag:
            return self.__dp(node.left,True)+self.__dp(node.right,True)
        return max(self.__dp(node.left,True)+self.__dp(node.right,True),self.__dp(node.left,False)+self.__dp(node.right,False)+node.val)

if __name__ == '__main__':
    so = Solution()
    # root = TreeNode(3)
    # root.left = TreeNode(2)
    # root.left.right = TreeNode(3)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(1)

    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(1)
    print(so.rob(root))