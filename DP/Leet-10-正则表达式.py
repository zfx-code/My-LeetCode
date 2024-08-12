"""
10. 正则表达式匹配

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 

提示：

1 <= s.length <= 20
1 <= p.length <= 20
s 只包含从 a-z 的小写字母。
p 只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        从左往右扫, 后边可能的"*"影响结果:
        从右往左扫, "*"前边一定有一个字符, 也只影响该字符

        p[j - 1] = "*"时, dp[i][j]取决于
        (1) dp[i][j - 2]: 将一对"p[j - 2]*"看做0次, []匹配之前的
        (2) dp[i - 1][j] == True and s[i - 1] == p[j - 2]:
            让p[j - 2]多出现1次
        (3) dp[i - 1][j] == True and p[j - 2] == ".":
            ".*"匹配字符
        
        p[j - 1] != "*"时:
        需要匹配
        """

        m, n = len(s), len(p) 

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True 

        # 当跟s空串匹配时, 偶数位置是"?*"可以表示0个, maybe匹配
        for j in range(2, n + 1, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 带注释版详写
                if p[j - 1] == "*":
                    # 三种情况
                    # (1) "*"和前一位等价于空串: ""进行匹配
                    c1 = dp[i][j - 2]
                    # (2) s回退一位, p无需回退, 一个"*"当2个用
                    # dp[i - 1][j]若为True, 表示p[j - 1]已经匹配到了s[i - 2]
                    # 就看是否能继续匹配s[i - 1], 两种情况:
                    # 虚假匹配".*" or 真实匹配 
                    c2 = dp[i - 1][j] and p[j - 2] == s[i - 1]
                    c3 = dp[i - 1][j] and p[j - 2] == "."
                    dp[i][j] = c1 or c2 or c3 
                else:
                    # 不为"*", 约束更大, 两种情况:
                    # 虚假匹配".*" or 真实匹配 
                    c1 = dp[i - 1][j - 1] and p[j - 1] == s[i - 1]
                    c2 = dp[i - 1][j - 1] and p[j - 1] == "."
                    dp[i][j] = c1 or c2 
                
                # 整理格式版本
                # if p[j - 1] == "*":
                #     c1 = dp[i][j - 2]
                #     c2 = dp[i - 1][j] and p[j - 2] in [s[i - 1], "."]
                #     dp[i][j] = c1 or c2
                # else:
                #     dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in [s[i - 1], "."]

        return dp[-1][-1]
    
"""
44. 通配符匹配

相关企业
给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符序列（包括空字符序列）。
判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。

示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2：

输入：s = "aa", p = "*"
输出：true
解释：'*' 可以匹配任意字符串。
示例 3：

输入：s = "cb", p = "?a"
输出：false
解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j]表示s前i个和p前j个是否匹配
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True
        # 只有全"*"才能匹配空串"" 
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = True 
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # 不用掉这个"*"(当做没有) or 用掉这个"*"
                    # eg: abb <-> a* (得看前一个字符是否也能被"*"匹配)
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in [s[i - 1], "?"]
        
        return dp[-1][-1]