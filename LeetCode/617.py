# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.__subMerge(t1,t2)

    def __subMerge(self,t1,t2):
        if t1==None and t2==None:
            return None
        if t1==None:
            return t2
        if t2==None:
            return t1

        tmp_Node = TreeNode(t1.val+t2.val)
        left = self.__subMerge(t1.left,t2.left)
        right = self.__subMerge(t1.right,t2.right)
        tmp_Node.left = left
        tmp_Node.right = right
        return tmp_Node

if __name__ == '__main__':
    so = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)
    t1.right = TreeNode(2)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)

    t=so.mergeTrees(t1,t2)
    print('fds')
