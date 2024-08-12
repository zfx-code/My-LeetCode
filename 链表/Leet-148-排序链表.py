"""

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

输入：head = [4,2,1,3]
输出：[1,2,3,4]

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

归并排序基于分治算法。最容易想到的实现方式是自顶向下的递归实现，考虑到递归调用的栈空间，自顶向下归并排序的空间复杂度是 O(log⁡n)。如果要达到 O(1) 的空间复杂度，则需要使用自底向上的实现方式。

方法一：自顶向下归并排序
对链表自顶向下归并排序的过程如下。

找到链表的中点，以中点为分界，将链表拆分成两个子链表。寻找链表的中点可以使用快慢指针的做法，快指针每次移动 2 步，慢指针每次移动 1 步，当快指针到达链表末尾时，慢指针指向的链表节点即为链表的中点。

对两个子链表分别排序。

将两个排序后的子链表合并，得到完整的排序后的链表。可以使用「21. 合并两个有序链表」的做法，将两个有序的子链表进行合并。

上述过程可以通过递归实现。递归的终止条件是链表的节点个数小于或等于 1，即当链表为空或者链表只包含 1 个节点时，不需要对链表进行拆分和排序。


作者：力扣官方题解
链接：https://leetcode.cn/problems/sort-list/solutions/492301/pai-xu-lian-biao-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 
23. 合并 K 个升序链表
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

################### myself ####################
# 迭代实现, 非递归, 返回head
def merge_Two_Lists(self, list1, list2):
    # 哑结点, 模拟head, 不怕None
    dummy_Node = ListNode(0)
    cur = dummy_Node 

    # 都不为None
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1 
            list1 = list1.next 
        else:
            cur.next = list2 
            list2 = list2.next 
        cur = cur.next 

    # 拼接剩余的, 最多1个非None
    if list1:
        cur.next = list1 
    else:
        cur.next = list2
    
    # 真正的头结点
    return dummy_Node.next 

# 递归合并[l, r]的全部(找到mid, 分别合成左半部分和右半部分)
def merge(self, lists: List[ListNode], l, r):
    if l > r:
        return None 
    if l == r:
        return lists[l]
    
    # 正式合并
    mid = (l + r) // 2 
    left = self.merge(lists, l, mid)
    right = self.merge(lists, mid + 1, r)
    return self.merge_Two_Lists(left, right)

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    return self.merge(lists, 0, len(lists) - 1)
"""

# 普通归并排序
# def merge_sort():

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
current = dummy.next;
tail = dummy;
for (step = 1; step < length; step *= 2) {
	while (current) {
		// left->@->@->@->@->@->@->null
		left = current;

		// left->@->@->null   right->@->@->@->@->null
		right = cut(current, step); // 将 current 切掉前 step 个头切下来。

		// left->@->@->null   right->@->@->null   current->@->@->null
		current = cut(right, step); // 将 right 切掉前 step 个头切下来。
		
		// dummy.next -> @->@->@->@->null，最后一个节点是 tail，始终记录
		//                        ^
		//                        tail
		tail.next = merge(left, right);
		while (tail->next) tail = tail->next; // 保持 tail 为尾部

"""
class Solution:
    # head切断前k个, 返回剩下的head
    def cut(self, head, k):
        cur = head 

        # 切前k个, 走k-1步即可
        while cur and k > 1:
            cur = cur.next 
            k -= 1 
        
        if cur == None:
            return None 
        
        last = cur.next 
        cur.next = None 

        return last

    # 升序合并2个有序链表
    def merge_Two_List(self, list1: ListNode, list2: ListNode):
        dummy = ListNode(0)
        cur = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next 
            else:
                cur.next = list2 
                list2 = list2.next 
            cur = cur.next 
        
        # 接上剩余的, list1, list2最多1个None
        if list1:
            cur.next = list1 
        else:
            cur.next = list2
        
        return dummy.next 
    
    def sortList(self, head: ListNode) -> ListNode:
        """
        eg: [4,3,1,7,8,9,2,11,5,6]
        step=1: (3->4)->(1->7)->(8->9)->(2->11)->(5->6)
        step=2: (1->3->4->7)->(2->8->9->11)->(5->6)
        step=4: (1->2->3->4->7->8->9->11)->5->6
        step=8: (1->2->3->4->5->6->7->8->9->11)
        
        merge(l1, l2): 合并2个有序
        cut(l, n)    : 断链, l切掉前n个节点, 返回剩下的head
        """
        dummy = ListNode(0)
        dummy.next = head

        # 获取总结点数
        n = 0
        cur = head 
        while cur:
            cur = cur.next 
            n += 1 

        step = 1
        while step <= n:
            cur = dummy.next 
            tail = dummy
            # step = 1, 合并的步长是2 * step = 2
            while cur:
                # left->#->...->None
                left = cur

                # left->#->None, right->#...->#->None
                right = self.cut(cur, step)

                # 此时len(left) = len(left) = step, 剩下的是cur
                cur = self.cut(right, step)

                # dummy.next->#->#->#->#->None
                #                      ^
                #                     tail, 维护最后的节点 
                # 返回的是head, 需要找到最后的
                tail.next = self.merge_Two_List(left, right)
                while tail.next:
                    tail = tail.next 
            
            step = step * 2

        return dummy.next

s = Solution()

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
# res = s.sortList(head)



res = s.cut(head, 1)

while res:
    print(res.val)
    res = res.next 
