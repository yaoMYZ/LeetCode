import numpy as np
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.__result = True
        pass

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.__valid(root)
        return self.__result

    def __valid(self,node):
        if not self.__result:
            return [np.inf, -np.inf]
        if node==None:
            return [np.inf,-np.inf]

        left_min, left_max = self.__valid(node.left)
        right_min, right_max = self.__valid(node.right)
        if node.val>= right_min or node.val<= left_max:
            self.__result = False
            return [np.inf, -np.inf]
        else:
            return [min(left_min,node.val),max(right_max,node.val)]

if __name__ == '__main__':
    so = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    # root.right = TreeNode(4)
    # root.right.left = TreeNode(3)
    # root.right.right = TreeNode(6)
    print(so.isValidBST(root))