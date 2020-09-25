# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.major = set()
        self.max_num = 0
        self.num_dict = {}
        pass

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        self.__subFind(root)
        return list(self.major)

    def __subFind(self,node):
        if node==None:
            return
        if node.val not in self.num_dict:
            self.num_dict[node.val] = 0
        self.num_dict[node.val]+=1
        if self.num_dict[node.val]>self.max_num:
            self.major.clear()
            self.major.add(node.val)
            self.max_num = self.num_dict[node.val]
        elif self.num_dict[node.val]==self.max_num:
            self.major.add(node.val)

        self.__subFind(node.left)
        self.__subFind(node.right)

if __name__ == '__main__':
    so = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    print(so.findMode(root))