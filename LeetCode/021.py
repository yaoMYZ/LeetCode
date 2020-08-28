# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(-1)
        cur_l3 = l3
        while l1!=None or l2!=None:
            if l1==None:
                cur_l3.next=l2
                break
            if l2==None:
                cur_l3.next=l1
                break
            if l1.val<l2.val:
                cur_l3.next=l1
                cur_l3 = cur_l3.next
                l1=l1.next
            else:
                cur_l3.next = l2
                cur_l3 = cur_l3.next
                l2 = l2.next
            pass
        return l3.next

if __name__ == '__main__':
    so = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = so.mergeTwoLists(l1,l2)
    while l3!=None:
        print(l3.val)
        l3=l3.next