# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.__subBuild(inorder,postorder)

    def __subBuild(self,inorder, postorder):
        if len(inorder)==0:
            return None
        node = TreeNode(postorder[-1])
        idx = self.__findIdx(inorder,postorder[-1])
        left_node = self.__subBuild(inorder[:idx],postorder[:idx])
        right_node = self.__subBuild(inorder[idx+1:],postorder[idx:-1])
        node.left = left_node
        node.right = right_node
        return node

    def __findIdx(self,inorder,val):
        for i in range(len(inorder)):
            if inorder[i]==val:
                return i

if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    so = Solution()
    root = so.buildTree(inorder, postorder)
    print('done')