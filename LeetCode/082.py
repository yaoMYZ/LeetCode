# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hhead = ListNode(-1)
        hhead.next = head
        h1 = hhead
        h2 = h1.next
        if h2==None:
            return head
        h3 = h2.next
        del_Flag = False
        while h3!=None:
            if h3.val==h2.val:
                del_Flag = True
                h2 = h3
                h3 = h3.next
            else:
                if del_Flag:
                    h2 = h3
                    h1.next = h2
                    h3 = h3.next
                    del_Flag = False
                else:
                    h1=h2
                    h2=h3
                    h3=h3.next
        if del_Flag:
            h1.next = None
        return hhead.next

if __name__ == '__main__':
    so = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(4)
    lnode = so.deleteDuplicates(head)
    while lnode!=None:
        print(lnode.val)
        lnode = lnode.next