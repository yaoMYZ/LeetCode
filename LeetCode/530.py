# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.__record = []
        self.__min_diff = 10e10

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.__get_min_diff(root)
        return self.__min_diff
    
    def __get_min_diff(self,node):
        if node==None:
            return
        for num in self.__record:
            self.__min_diff = min(self.__min_diff,abs(node.val-num))
        self.__record.append(node.val)
        self.__get_min_diff(node.left)
        self.__get_min_diff(node.right)
