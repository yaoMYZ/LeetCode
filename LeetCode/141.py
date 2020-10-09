# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_set = set()
        while head!=None:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False

if __name__ == '__main__':
    so = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    print(so.hasCycle(head))