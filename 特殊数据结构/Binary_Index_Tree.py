"""
树状数组(Binary Index Tree, BIT)
对于一个数组arr, 元素个数很多
(1) 修改一个值O(1)
(2) 求一段区间的和O(n)
需要改进到O(log(n))

前缀和会交换这两个操作对应的复杂度

树状数组利用二进制
维护区间-(1) 修改不需要更新太多区间 (2) 查询不需要组合太多区间
eg: 11 -> (1011)_2, 求前11项的和
分别查询3个区间:
(0000, 1000], (1000, 1010], (1010, 1011]
不断去掉11的二进制最右边1的过程
(1) 101"1" -> (1010, 1011]
(2) 10"1"0 -> (1000, 1010]
(3) "1"000 -> (0000, 1000]

定义二进制数x最右边的1连着之后的0, 为lowbit(x)
则C[i]表示区间(A[i] - lowbit(A[i]), A[i]]
"""


# 最后一个1连着之后的0对应的数
# eg: 111000 -> 11|1000 -> 8
def lowbit(x: int) -> int:
    # -x是把x按位取反再+1, eg: *1000 -> *0111 -> (~*)1000
    # 再与x按位与, 前边的都成0了, 留下了最后的1带着0
    return x & (-x)

# 位置修改arr[p] = x, 对应修改数组b
def update(tree_arr: list[int], i: int, x: int) -> None:
    N = len(tree_arr)
    while i < N:
        tree_arr[i] += x 
        i           += lowbit(i)

# 前i项和
def count_n(tree_arr: list[int], i: int) -> int:
    res = 0 
    while i > 0:
        res += tree_arr[i]
        i   -= lowbit(i)    
    return res

# 区间查询arr[a]+...+arr[b]
# count_n(tree_arr, a - 1, b)
arr = [1, 2, 3, 4, 5]
tree_arr = [0 for i in range(6)]

for i in range(1, 6):
    update(tree_arr, i, arr[i - 1])

# print(tree_arr)
print(count_n(tree_arr, 4) - count_n(tree_arr, 3))


"""
求解逆序对问题

(1) 离散化, [1, 5, 3, 8, 999]不需要开999这么大的空间 
新开数组d, d[i]存放第i大的数在原序列的位置(+1)
eg: a = [5, 3, 4, 2, 1]
    d = [1, 3, 2, 4, 5]
转换之后, d的正序对就是要求原a的逆序对
    把1放到arr_tree中, 此时t有1个数1, 没有比1小的,              ans += 0 
    把3放到arr_tree中, 此时t有2个数1, 3, 比3小的数1个,          ans += 1 
    把2放到arr_tree中, 此时t有3个数1, 2, 3, 比2小的数1个,       ans += 1 
    把4放到arr_tree中, 此时t有3个数1, 2, 3, 4, 比4小的数3个,    ans += 3
    把5放到arr_tree中, 此时t有5个数1, 2, 3, 4, 5, 比5小的数4个, ans += 4
抽象, 每次把x放进去, 查询[1, x-1]里有几个数已经在arr_tree
arr_tree[x]表示为[1, x]中有几个数存在
每次放进去x, 更新包含x的节点, 后查询[1, x-1]有多少数
"""

# 按照大小对索引排序, 从大到小(逆序)
a = [5, 3, 4, 2, 1]

d = sorted([i + 1 for i in range(len(a))], key = lambda x: a[x - 1], reverse=True)
print(d)