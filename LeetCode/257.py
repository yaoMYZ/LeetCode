# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root==None:
            return []
        str_list = self.findPaths(root)
        return str_list

    def findPaths(self,node):
        if node.left==None and node.right==None:
            return [str(node.val)]
        str_list = []
        if node.left!=None:
            str_arr = self.findPaths(node.left)
            for row in str_arr:
                row = str(node.val)+'->'+row
                str_list.append(row)
        if node.right!=None:
            str_arr = self.findPaths(node.right)
            for row in str_arr:
                row = str(node.val) + '->' + row
                str_list.append(row)
        return str_list

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    print(Solution().findPaths(root))


