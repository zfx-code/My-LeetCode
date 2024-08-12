# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def rec_reverse(head):
            if not head or not head.next:
                return head 
            
            new_head = rec_reverse(head.next)
            head.next.next = head 
            head.next = None

            return new_head 
        
        # (1) 找到中间节点, 快慢指针
        slow, fast = head, head 

        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next

        # fast跑出去了, 偶数个
        # 否则奇数个fast将处于最后1个节点
        # if fast:
        #     slow = slow.next  
        # print(f"fast: {fast.val}")
        print(f"slow: {slow.val}")
        # 前后半段
        left = head 
        right = rec_reverse(slow)

        print(left.val)
        print(right.val)
        while right != None:
            if left.val != right.val:
                return False 
            left = left.next 
            right = right.next

        return True 

a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

s = Solution()

print(s.isPalindrome(head=a))