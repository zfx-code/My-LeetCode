def minWindow(s: str, t: str) -> str:
        hashtable = dict()

        ans = "#" * 100000
        # target
        for ti in t:
            if ti in hashtable:
                hashtable[ti] += 1 
            else:
                hashtable[ti] = 1
        
        # 距离target还差多少
        cnt = len(t)

        i = 0
        n = len(s)
        
        for j in range(n):
            # print(f"cnt: {cnt}, s[j] : {s[j]}")
            # hashtable["?"]=k刻画还需要"?"还需要k个
            if s[j] in hashtable:
                hashtable[s[j]] -= 1
                if hashtable[s[j]] >= 0:
                    cnt -= 1
       
            if cnt > 0:
                continue 
            # print("当前有一组可行解[i, j+1], i->", s[i:j+1])
            # 这是一个可行解, 需要缩短边界
            while True:
                # print(hashtable)
                # 非target字符
                if s[i] not in hashtable:
                    i += 1
                # target字符
                else:
                    hashtable[s[i]] += 1
                    # 当前所需 > 0, 此时的s[i]必须包含进来
                    if hashtable[s[i]] > 0:
                        cnt += 1
                        break
                    # 是target, 但重复, 可以删除
                    else:
                        i += 1
             
            if j - i + 1 < len(ans):
                ans = s[i:j+1]
 
            i += 1

        if ans == "#" * 100000:
            return ""
        
        return ans

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))
