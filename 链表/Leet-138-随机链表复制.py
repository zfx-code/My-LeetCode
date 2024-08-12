"""
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

本题难点： 在复制链表的过程中构建新链表各节点的 random 引用指向
def copyRandomList(self, head: 'Node') -> 'Node':
    cur = head
    dum = pre = Node(0)
    while cur:
        node = Node(cur.val) # 复制节点 cur
        pre.next = node      # 新链表的 前驱节点 -> 当前节点
        # pre.random = '???' # 新链表的 「 前驱节点 -> 当前节点 」 无法确定
        cur = cur.next       # 遍历下一节点
        pre = node           # 保存当前新节点
    return dum.next

方法二：拼接 + 拆分
考虑构建 原节点 1 -> 新节点 1 -> 原节点 2 -> 新节点 2 -> …… 的拼接链表，如此便可在访问原节点的 random 指向节点的同时找到新对应新节点的 random 指向节点。

算法流程：
(1) 复制各节点，构建拼接链表：设原链表为
node1 -> node2 -> ...
新的拼接链表为
node1 -> node1_new -> node2 -> node2_new -> ...

(2) 构建新链表各节点的 random 指向：当访问原节点 cur 的随机指向节点 cur.random 时，对应新节点 cur.next 的随机指向节点为 cur.random.next 。

(3) 拆分原 / 新链表：设置 pre / cur 分别指向原 / 新链表头节点，遍历执行 pre.next = pre.next.next 和 cur.next = cur.next.next 将两链表拆分开。

(4) 返回新链表的头节点 res 即可

# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 使用hashtable方案
def copyRandomList(head: Node) -> Node:
    if head == None:
        return None
    # 映射为 {原节点 : 新节点}
    hashtable = dict()
    hashtable[None] = None
    cur = head 
    while cur != None:
        # 新节点目前只存val
        hashtable[cur] = Node(cur.val)
        cur = cur.next 
    
    cur = head 
    # 构建新节点的next和random朝向
    while cur != None:
        hashtable[cur].next = hashtable[cur.next]
        hashtable[cur].random = hashtable[cur.random]
        cur = cur.next 

    return hashtable[head]

# 使用hashtable方案
def copyRandomList_without_hashtable(head: Node) -> Node:
    if head == None:
        return None

    cur = head 
    # (1) 拼接old_new
    while cur != None:
        tmp = Node(cur.val, cur.next)
        cur.next = tmp 
        # 连跳两次
        cur = cur.next.next 

    cur = head 
    # (2) 构建新节点的random朝向
    while cur != None:
        if cur.random != None:
            # 此时是原节点(cur.next是新节点)
            # cur.random是原节点, 再next是对应的新节点
            cur.next.random = cur.random.next
        cur = cur.next.next 

    # (3) 拆分原/新链表 
    new_head = head.next 
    pre = head
    # 新
    cur = head.next  
    while cur.next != None:
        pre.next = pre.next.next 
        cur.next = cur.next.next 
        pre = pre.next 
        cur = cur.next 
    # 彻底拆分两个
    pre.next = None 

    return new_head