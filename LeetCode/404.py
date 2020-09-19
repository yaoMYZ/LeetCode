# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        return self.__sum(root,1)

    def __sum(self,node,pos):
        if node.left==None and node.right==None:
            if pos==0:
                return node.val
            else:
                return 0
        val=0
        if node.left!=None:
            val+=self.__sum(node.left,0)
        if node.right!=None:
            val+=self.__sum(node.right,1)
        return val

if __name__ == '__main__':
    so = Solution()
    print(so.sumOfLeftLeaves())