# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.find_node = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.__subFind(root,p,q)
        return self.find_node


    def __subFind(self,node,p,q):
        if self.find_node!=None:
            return False
        if node==None:
            return False

        flag_left = self.__subFind(node.left,p,q)
        flag_right = self.__subFind(node.right,p,q)
        if node.val == p.val or node.val == q.val:
            if flag_left^flag_right:
                self.find_node=node
                return False
            else:
                return True

        if flag_left and flag_right:
            self.find_node = node
            return False

        return flag_right^flag_left

if __name__ == '__main__':
    so = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = TreeNode(2)
    q = TreeNode(4)

    node = so.lowestCommonAncestor(root,p,q)
    print(node.val)