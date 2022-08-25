from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 添加新的头，是为了防止链表只有一个结点时，出现null = null.next的现象
        pre_head = ListNode(0)          # 定义一个临时节点
        pre_head.next = head            # 将链表挂在临时节点上，临时节点成为头节点
        slw = fst = pre_head            # 快慢指针开始位置都是临时节点

        i = 0
        while i <= n and fst:           # 快指针提前走n+1步，走到原链表第n个位置
            fst = fst.next
            i += 1

        while fst:                      # 快慢指针同时走，直到快指针走到链表末尾
            fst = fst.next
            slw = slw.next

        slw.next = slw.next.next        # 把慢指针的下一个节点（倒数第n个节点）删除
        return pre_head.next

        return new_.next


head = [1,2,3,4]
print(Solution().removeNthFromEnd(head,2))