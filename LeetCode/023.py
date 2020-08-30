# Definition for singly-linked list.

from queue import PriorityQueue as PQ
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result_ln = ListNode(-1)
        cur_ln = result_ln
        tmp_pq = PQ()
        for index, l in enumerate(lists): #python3 不允许插入优先级相同的值或者是无法判断优先级的值到优先队列,插入的时候加入一个index,就不会出现优先级相同的情况了。
            if l:
                tmp_pq.put([l.val, index, l])
        while tmp_pq.qsize()!=0:
            var,index,node = tmp_pq.get()
            cur_ln.next = node
            cur_ln = cur_ln.next
            node = node.next
            if node:
                tmp_pq.put([node.val,index,node])
            pass
        return result_ln.next

if __name__ == '__main__':
    lists = [[1,4,5],[1,3,4],[2,6]]
    lists_node = []
    for list in lists:
        l = ListNode(-1)
        c_l = l
        for t_l in list:
            c_l.next = ListNode(t_l)
            c_l = c_l.next
        lists_node.append(l.next)
    so = Solution()
    ln = so.mergeKLists(lists_node)
    while ln!=None:
        print(ln.val)
        ln = ln.next