# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution(object):
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head==None:
#             return None
#         tmp_arr = []
#         while head!=None:
#             tmp_arr.append(head)
#             head = head.next
#         self.__quick_sort(tmp_arr,0,len(tmp_arr)-1)
#         head = tmp_arr[0]
#         tmp_arr[-1].next = None
#         tmp = head
#         for i in range(1,len(tmp_arr)):
#             tmp.next = tmp_arr[i]
#             tmp = tmp.next
#         return head
#
#
#     def __quick_sort(self,arr,sidx,eidx):
#         if sidx>=eidx:
#             return
#         head = sidx
#         end = eidx+1
#         idx = sidx+1
#         bound = arr[sidx]
#         while idx<end:
#             if arr[idx].val<=bound.val:
#                 idx+=1
#                 head+=1
#             else:
#                 end -=1
#                 tmp = arr[end]
#                 arr[end] = arr[idx]
#                 arr[idx] = tmp
#
#         tmp = arr[head]
#         arr[head] = arr[sidx]
#         arr[sidx] = tmp
#         self.__quick_sort(arr,sidx,head-1)
#         self.__quick_sort(arr,head+1,eidx)

# class Solution:
#     def sortList(self, head):
#         if not head or not head.next: return head # termination.
#         # cut the LinkedList at the mid index.
#         slow, fast = head, head.next
#         while fast and fast.next:
#             fast, slow = fast.next.next, slow.next
#         mid, slow.next = slow.next, None # save and cut.
#         # recursive for cutting.
#         left, right = self.sortList(head), self.sortList(mid)
#         # merge `left` and `right` linked list and return it.
#         h = res = ListNode(0)
#         while left and right:
#             if left.val < right.val: h.next, left = left, left.next
#             else: h.next, right = right, right.next
#             h = h.next
#         h.next = left if left else right
#         return res.next


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(mid)
        new_head = res = ListNode(-1)
        while left and right:
            if left.val<right.val:
                new_head.next = left
                left = left.next
            else:
                new_head.next = right
                right = right.next
            new_head = new_head.next
        new_head.next = right if left==None else left
        return  res.next


if __name__ == '__main__':
    so = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(1)

    head = so.sortList(head)
    print(head)
