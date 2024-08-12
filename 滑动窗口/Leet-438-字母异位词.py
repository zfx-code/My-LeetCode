"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)

        if n < m:
            return []
        
        # count[i] > 0表示i字母需求几个
        count = [0 for _ in range(26)]
        for i in range(m):
            count[ord(p[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1

        # 有需求的字母类别数(不是总数), 比如a缺10个differ=1
        differ = len([c for c in count if c != 0])
        
        ans = []
        if differ == 0:
            ans.append(0)
        # 维护一个长度为len(p)的窗口
    
        # differ只有在0-1跳跃的时候才会变
        # 2,3,4只是小打小闹
        for i in range(n - m):
            # 旧的left, 新的right(相比原来移动了1位)
            left, right = ord(s[i]) - 97, ord(s[i + m]) - 97
            # left本来就是多余的, 扔了正好
            if count[left] == -1:
                differ -= 1
            # 本来正好, 现在少了 
            elif count[left] == 0:
                differ += 1
            # 需求
            count[left] += 1

            # 本来正好, 现在多了
            if count[right] == 0:
                differ += 1
            # 刚好缺这一个
            elif count[right] == 1:
                differ -= 1
            count[right] -= 1 

            if differ == 0:
                ans.append(i + 1)
        
        return ans
            







