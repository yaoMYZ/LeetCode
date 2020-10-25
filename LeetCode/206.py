# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        pre = head
        tmp = head.next
        head.next = None
        while tmp!=None:
            new_tmp = tmp.next
            tmp.next = pre
            pre = tmp
            tmp = new_tmp
        return pre

if __name__ == '__main__':
    so = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root = so.reverseList(root)
    print(root)

