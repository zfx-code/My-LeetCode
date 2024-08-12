"""
316. 去除重复字母

给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的
字典序
最小（要求不能打乱其他字符的相对位置）。

 
示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成
单调栈
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
       
        import collections 
         # 记录字母的剩余次数(>1可丢弃)
        hashtable = collections.Counter(s)

        stack = []

        for c in s:
            if c not in stack:
                while len(stack) > 0 and c < stack[-1] and hashtable[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            hashtable[c] -= 1 
        
        return "".join(stack)

"""
402. 移掉 K 位数字

给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

示例 1 ：

输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
示例 2 ：

输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 ：

输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n <= k:
            return "0"
        
        stack = []

        for i in range(n):
            a = int(num[i])
            # 维护一个单调不减 eg: [1,2,2,3...]
            while len(stack) > 0 and a < stack[-1] and k > 0:
                stack.pop()
                k -= 1 
            
            # 0不需要进入空栈
            if len(stack) == 0 and a == 0:
                continue 
            stack.append(a)
        
        # k还没消耗完, 继续扔掉最后的份额 
        while len(stack) and k > 0:
            stack.pop()
            k -= 1 
        
        if len(stack) == 0:
            return "0"
        
        # 拼接出结果 
        return "".join([str(a) for a in stack])
