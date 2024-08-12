"""
最近最少使用, 哈希表+双向链表实现
python的库collections.OrderedDict可以直接实现

"""


# Python 语言中，有一种结合了哈希表与双向链表的数据结构 OrderedDict
# class LRUCache(collections.OrderedDict):

#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity


#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)

# 双向链表, 可以向前和向后
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key   = key
        self.value = value
        self.prev  = None
        self.next  = None

# Hash+双向链表
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        # 使用哑head和tail避免额外判断
        # 初始时候只有head <-> tail
        # 随着insert会修改双指针
        self.head.next = self.tail
        self.tail.prev = self.head

        # max容量
        self.capacity = capacity
        # 当前容量
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # key存在, 使用hash表定位, 再移动到head
        node = self.cache[key]
        self.move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 不存在, 创建一个新节点
            node = DLinkedNode(key, value)
            # 加进hash表
            self.cache[key] = node
            # 加进双向链表head
            self.add_to_head(node)
            self.size += 1

            if self.size > self.capacity:
                # 超过容量, 删除尾节点
                removed = self.removeTail()
                # 删除hash表对应的key-value
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # key存在, 使用hash表定位, 再修改值, 再移动到head
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        # dummyhead <-> a ...
        # 变成dummyhead <-> node <-> a ...
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.removeNode(node)
        self.add_to_head(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)

        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
