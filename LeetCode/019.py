# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        hhead = ListNode(0)
        hhead.next = head
        fnode = hhead
        snode = fnode
        first_run = True
        idx = 0
        while fnode!=None:
            for idx in range(n):
                fnode=fnode.next
                if fnode==None:
                    break
            if fnode==None:
                break
            elif first_run:
                first_run=False
                continue
            else:
                for idx in range(n):
                    snode = snode.next

        for i in range(idx):
            snode = snode.next
        tmp = snode.next.next
        snode.next = tmp
        return hhead.next

if __name__ == '__main__':
    so = Solution()
    node = ListNode(1)
    # node.next = ListNode(2)
    # node.next.next = ListNode(3)
    # node.next.next.next = ListNode(4)
    # node.next.next.next.next = ListNode(5)
    result = so.removeNthFromEnd(node,1)
    print(result)