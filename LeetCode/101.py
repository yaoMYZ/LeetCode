# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        tmp_arr = [root]
        while len(tmp_arr)!=0:
            tmp_len = len(tmp_arr)
            new_arr = []
            for i in range(tmp_len//2):
                if tmp_arr[i].val != tmp_arr[tmp_len-i-1].val:
                    return False
            for i in range(tmp_len):
                if tmp_arr[i].val==10e10:
                    continue
                if tmp_arr[i].left!=None:
                    new_arr.append(tmp_arr[i].left)
                else:
                    new_arr.append(TreeNode(10e10))
                if tmp_arr[i].right != None:
                    new_arr.append(tmp_arr[i].right)
                else:
                    new_arr.append(TreeNode(10e10))
            tmp_arr = new_arr
        return True


if __name__ == '__main__':
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.left = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)

    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)

    root.right.right.left = TreeNode(9)
    root.right.right.right = TreeNode(8)
    so = Solution()
    print(so.isSymmetric(root))
