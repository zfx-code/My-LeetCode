"""
3. 无重复字符的最长子串
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        ans = 1
        # 滑动窗口的思路(窗口内不含重复字符)
        # 更新ans时仅当最新的1位跟之前的不重复
        # 记录不重复字符的位置
        hashtable = dict()
        left = 0 
        hashtable[s[left]] = left 
        
        for right in range(1, n):
            # 判断是否和窗口内重复(曾经出现)
            # 更新左边界
            if s[right] in hashtable:
                left = max(left, hashtable[s[right]] + 1)
            # 更新右边界
            hashtable[s[right]] = right 
            ans = max(ans, right - left + 1)

        return ans