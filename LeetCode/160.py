# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        fa = True
        fb = True
        while ha != hb:
            if ha:
                ha = ha.next
            elif fa:
                ha = headB
                fa = False
            else:
                return None

            if hb:
                hb = hb.next
            elif fb:
                hb = headA
                fb = False
            else:
                return None
        return ha

if __name__ == '__main__':
    ha = ListNode(1)
    hb = ListNode(2)
    hb.next = ListNode(3)
    so = Solution()
    print(so.getIntersectionNode(ha,hb))
