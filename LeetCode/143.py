# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        tmp_arr = []
        tmp_node = head
        while tmp_node!=None:
            tmp_arr.append(tmp_node)
            tmp_node = tmp_node.next
        mid_idx = len(tmp_arr)//2
        arr_len = len(tmp_arr)
        cur_node = ListNode(-1)
        for i in range(mid_idx):
            cur_node.next=tmp_arr[i]
            cur_node.next.next = tmp_arr[arr_len-i-1]
            cur_node = cur_node.next.next
        if len(tmp_arr)%2==1:
            cur_node.next = tmp_arr[mid_idx]
            cur_node = cur_node.next
        cur_node.next = None

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)

    so = Solution()
    so.reorderList(root)
    print(root)