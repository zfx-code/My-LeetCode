# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_ListNode(self):
        head = self
        while head != None:
            print(f"{head.val}->", end="")
            head = head.next
        
        print("\n")

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head
    # pre存的是 [cur : cur.pre]
    # 即pre[a.next] = a 
    pre = dict()
    cur = head 
    start, end = None, None
    before, after = None, None  
    i = 0
    node_list = []
    while cur != None:
        node_list.append(cur)
        # pre[cur.next] = cur 
        
        # if i == left - 1:
        #     start = cur 
        #     if start != None:
        #         print("start.val: ", start.val)
        #     before = pre[start]
        # if i == right - 1:
        #     end = cur
        #     if end != None:
        #         print("end.val: ", end.val)
            
        #     after = end.next 
        # i += 1 
        cur = cur.next 
    
    # 分为before + [left, right] + after
    # 翻转中间[left, right]的, 再拼接
        print([node.val for node in node_list])
    node_list = node_list[:left-1] + node_list[left-1:right][::-1] + node_list[right:] 
    print([node.val for node in node_list])
    # 重构next
    for i in range(len(node_list)-1):
        cur = node_list[i]
        cur.next = node_list[i+1]
    node_list[-1].next = None
    return node_list[0]
    # old_start = start
    # while start != end:
    #     tmp = start.next 
    #     start.next = pre[start]
    #     start = tmp 
    # # 此时start是原end, 且来到了开头
    # start.next = pre[start]
    # before.next = start 
    # old_start.next = after 

    # return head
    
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = ListNode(3, ListNode(5))
left = 1
right = 2 
head = reverseBetween(head, left, right)

print("#####")

# 生成链表
def gen_ListNode(nums):
    head = ListNode(nums[0])
    cur = head

    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        cur.next = node 
        cur = node 
    
    return head 

# def print_ListNode(head):
#     while head != None:
#         print(f"{head.val}->")
#         head = head.next

# (1) 递归反转链表-全部
# A->B->C => C->B->A
# return C(反转后的头结点)
def rec_reverse(head):
    # 防止扔进来空的
    # if head == None:
    #     return None 
    if head.next == None:
        return head
    
    # 原来的last是现在的head
    last = rec_reverse(head.next)
    # 原来是1->2->..., 现在是...->2->1
    head.next.next = head 
    head.next = None

    return last

# (2) 递归反转链表前n个节点, n<=总长度
# eg: 1->2->3->4->5, n=3
# return new head "3"
# (3->2->1)->4->5
def rec_reverse_N(head, n):
    if n == 1:
        return head

    last = rec_reverse_N(head.next, n - 1)
    # 此时后继successor是接在"2"后边
    # 1->3(last)->2->(4->5)(successor)
    successor = head.next.next
    head.next.next = head 
    # 尾巴接上 "4->5"
    head.next = successor

    return last 

# (2) 递归反转链表某个区间[left, right], 从1开始
# eg: 1->2->3->4->5, left=3, right=4
# return new head "1"
# 1->2->(4->3)->5
def rec_reverseBetween(head, left, right):
    # base case
    if left == 1:
        return rec_reverse_N(head, right)

    # left > 1 
    head.next = rec_reverseBetween(head.next, left - 1, right - 1)
    return head



head = gen_ListNode([1,2,3,4,5])
head.print_ListNode()

# head = rec_reverse_N(head, 3)
head = rec_reverseBetween(head, 2, 3)
head.print_ListNode()

