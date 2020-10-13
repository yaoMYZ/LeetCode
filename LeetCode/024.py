# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first_node = ListNode(-1)
        first_node.next = head
        op_node = first_node
        while op_node.next!=None and op_node.next.next!=None:
            node1 = op_node.next
            node2 = node1.next
            node1.next = node2.next
            node2.next = node1
            op_node.next = node2
            op_node = node1
        return first_node.next