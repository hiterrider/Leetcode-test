# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_linklist_head(self,li):
        head = ListNode(li[0])  # 头结点
        for element in li[1:]:
            node = ListNode(element)
            node.next = head
            head = node
        return head

    # 遍历输出链表：
    def print_linklist(self,li):
        while li:
            print(li.val, end=',')
            li = li.next
        print(end='\n')

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)  # 新建链表头结点
        cur = result  # 头结点
        next1 = 0  # 进位
        while (l1  or l2 ):  # l1或l2有一个存在即可
            x = l1.val if l1 else 0  # l1当前节点的值
            y = l2.val if l2 else 0  # l2当前节点的值
            total = next1 + x + y  # 进位加l1和l2的值
            next1 = total // 10  # 判断是否进位
            cur.next = ListNode(total%10)  # 去和的个位部分
            cur=cur.next  # 指向下一个节点
            if(l1!=None): l1=l1.next  # 若l1不为空，则l1指向下一个节点
            if(l2!=None): l2=l2.next  # 若l2不为空，则l2指向下一个节点
        if(next1>0):  # 如果最后还存在进位
            cur.next = ListNode(1)  # 创键新节点用来存储最高位
        return result.next  # 返回头结点之后的节点，头结点未参与计算

node1 = ListNode().create_linklist_head([9,9,9,9,9])
ListNode().print_linklist(node1)
node2 = ListNode().create_linklist_head([9, 9])
ListNode().print_linklist(node2)

result = Solution().addTwoNumbers(node1,node2)
ListNode().print_linklist(result)