class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # 长度为m的子串编码
        # hash[i+1]表示以s[i]结尾的长为m的子串s[i-m+1:i+1], hash[0]=0
        # 递推关系(加入s[i], 去掉s[i-m])
        # hash[i+1]=hash[i]*base-encode(s[i-m])*base^m+encode(s[i])
        # base^m可预计算为一个数组, mul[i]=base^i 

        n = len(s)
        MOD = 10**9 + 7
        # 双哈希, 防止碰撞
        base1, base2 = 31, 71

        encode = {}
        for i in range(26):
            encode[chr(ord('a') + i)] = i 
        
        # check函数
        # def check(m, s, base1, base2):
        

        #     power1 = pow(base1, m, mod)
        #     power2 = pow(base2, m, mod)

        #     for i in range(m, n):
        #         hash_val1 = (hash_val1 * base1 - encode[s[i - m]] * power1 + encode[s[i]]) % mod 
        #         hash_val2 = (hash_val2 * base2 - encode[s[i - m]] * power2 + encode[s[i]]) % mod 

        #         if (hash_val1, hash_val2) in visited:
        #             # 起始位置, 长度
        #             return i - m + 1, m
        #     # 没找到
        #     return -1, 0
        def check(m, s, base1, base2):
            n = len(s)
            hash_val1, hash_val2 = 0, 0
            visited = set()

            for i in range(m):
                hash_val1 = (hash_val1 * base1 + encode[s[i]]) % MOD 
                hash_val2 = (hash_val2 * base2 + encode[s[i]]) % MOD
            visited.add((hash_val1, hash_val2))
            
            power1 = pow(base1, m, MOD)
            power2 = pow(base2, m, MOD)

            for i in range(m, n):
                hash_val1 = (hash_val1 * base1 - encode[s[i - m]] * power1 + encode[s[i]]) % MOD 
                hash_val2 = (hash_val2 * base2 - encode[s[i - m]] * power2 + encode[s[i]]) % MOD

                if (hash_val1, hash_val2) in visited:
                    # 起始位置, 长度
                    return i - m + 1, m
                visited.add((hash_val1, hash_val2))

            return -1, 0


        # 二分搜索(向右搜索
        low, high = 0, n 
        max_len = 0
        start = -1
        while low < high:
            mid = low + ((high - low) // 2)
            print(low, high, mid)
            idx, tmp_len = check(mid, s, base1, base2)
            if idx != -1:
                low = mid + 1 # 保存一个可行解 bisect_right
                start, size = idx, tmp_len 
            else:
                high = mid  
        
        return s[start:start+size] if start != -1 else ""

        '''二分搜索【往右搜模板】'''
        # left, right = 0, n
        # size = 0
        # start = -1
        # while left < right:
        #     mid = (left+right) // 2
        #     print(left, right, mid)
        #     idx, tmp_len = check(mid, s, base1, base2)
        #     if idx != -1:
        #         left = mid+1    # 【往右搜：bisect_right】
        #         start, size = idx, tmp_len
        #     else:
        #         right = mid
        
        # return s[start:start+size] if start != -1 else ''

s = Solution()

s.longestDupSubstring("banana")