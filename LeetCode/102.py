# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        tmp_arr = [root]
        all_record = []
        while len(tmp_arr)!=0:
            new_arr = []
            record = []
            for node in tmp_arr:
                record.append(node.val)
                if node.left!=None:
                    new_arr.append(node.left)
                if node.right!=None:
                    new_arr.append(node.right)
            all_record.append(record)
            tmp_arr=new_arr
        return all_record
