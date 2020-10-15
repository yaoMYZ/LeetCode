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
        tmp_arr = [root]
        while len(tmp_arr)!=0:
            new_arr = []
            tmp_arr.append(None)
            for idx in range(len(tmp_arr)-1):
                tmp_arr[idx].next = tmp_arr[idx+1]
                if tmp_arr[idx].left!=None:
                    new_arr.append(tmp_arr[idx].left)
                if tmp_arr[idx].right!=None:
                    new_arr.append(tmp_arr[idx].right)
            tmp_arr = new_arr
        return root

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    so = Solution()
    so.connect(root)
    print(root)