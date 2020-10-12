# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.__build(preorder,inorder)

    def __build(self,preorder, inorder):
        if len(preorder)==0:
            return None
        new_node = TreeNode(preorder[0])
        parent = preorder[0]
        idx = 0
        while inorder[idx]!=parent:
            idx+=1
        new_node.left = self.__build(preorder[1:idx+1],inorder[:idx])
        new_node.right = self.__build(preorder[idx+1:],inorder[idx+1:])

        return new_node

if __name__ == '__main__':
    so = Solution()
    root = so.buildTree([1,2],[1,2])
    print(root)
