"""
KMP算法
主串s      : 长度n, 指针i
子串target : 长度m, 指针j

正常情况下一旦有一位不匹配, 则全部回退i, j
最坏情况O(mn)

KMP精髓, 指针i不回退, 复杂度O(n)
维护一个next数组, 使得匹配失败后查询子串可以跳过的匹配个数

next数组的本质是寻找最长公共前后缀, 信息包含在target里
next[i]指的是以i字符结尾的子串的最长公共前缀
"""


def build_next(target):
    next = [0]
    # 当前公共前后缀的长度
    prefix_len = 0
    i = 1 

    while i < len(target):
        if target[prefix_len] == target[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1 
        # 匹配失败, 重复检索next
        else:
            if prefix_len == 0:
                next.append(0)
                i += 1 
            else:
                prefix_len = next[prefix_len - 1]
    
    return next


def kmp_search(s, target):
    next = build_next(target=target)

    # 主串的指针
    i = 0
    # 子串的指针
    j = 0 

    while i < len(s):
        if s[i] == target[j]:
            i += 1 
            j += 1 
        # 匹配失败, next跳过一些子串字符
        elif j > 0:
            j = next[j - 1]
        # 第一个字符即失败
        else:
            i += 1 
        
        if j == len(target):
            return i - j 
    
    # 匹配失败
    return -1

haystack = "sadbutsad"
needle = "sad"

# print(kmp_search(s=haystack, target=needle))
print(build_next("abcabcd"))



def build_next(target: str):
    n = len(target)
    # next[i] 表示以i结尾的最长公共前缀长度
    next = [0]

    prefix_len = 0 

    i = 1

    while i < n:
        if target[prefix_len] == target[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            if prefix_len == 0:
                next.append(0)
                i += 1
            else:
                prefix_len = next[prefix_len - 1]


