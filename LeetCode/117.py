
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None:
            return None
        tmp_stack = [root,None]
        while len(tmp_stack)!=0:
            new_stack = []
            for i in range(len(tmp_stack)-1):
                tmp_stack[i].next = tmp_stack[i+1]
                if tmp_stack[i].left!=None:
                    new_stack.append(tmp_stack[i].left)
                if tmp_stack[i].right!=None:
                    new_stack.append(tmp_stack[i].right)
            if len(new_stack)>0:
                new_stack.append(None)
            tmp_stack = new_stack
        return root

