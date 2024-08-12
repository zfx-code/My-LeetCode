class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 生成链表
def gen_ListNode(nums):
    head = ListNode(nums[0])
    cur = head

    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        cur.next = node 
        cur = node 
    
    return head 

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head 
        nodes = dict()
        n = 0
        while cur:
            nodes[n] = cur 
            n += 1 
            cur = cur.next
        if k == 1 or n < k:
            return head
        
        # 每一段的[head, tail]
        pairs = []

        print(f"n: {n}, k: {k}")
        # 每次处理k个
        for i in range(n//k):
            # i : i + k
            pairs.append([nodes[i*k + k - 1], nodes[i*k]])
            print(f"##### {i}")
            print(pairs[-1][1].val)
            print(pairs[-1][0].val)
            for j in range(k-1):
                nodes[i*k + k - 1 - j].next = nodes[i*k + k - 1 - j - 1]
        
        # 拼起来
        for i in range(n//k - 1):
            # print(f"head: {pairs[i][0].val}, tail: {pairs[i][1].val}")
            print(f"tail: {pairs[i][1].val} -> head: {pairs[i+1][0].val}")
            pairs[i][1].next = pairs[i+1][0]
        
        # # 最后一段<k的结果
        last = None 
        if n - (n % k) in nodes:
            last = nodes[n-(n % k)]
        pairs[-1][1].next = last
        # print(pairs[-1][1].val)
        # print(pairs[-1][0].val)

        return pairs[0][0]
            


head = gen_ListNode([1,2])
s = Solution()

res = s.reverseKGroup(head=head, k=2)

while res:
    print(res.val)
    res = res.next