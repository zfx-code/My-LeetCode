# 最长回文子串, 中心扩展法
def center_method(s):
    # 填充后, 单边扩展长度 = 回文长度
    s = "^#" + "#".join(s) + "#$"
    n = len(s)
    # 长度, 若需要回文串, 只需记录起点(注意考虑"^#$"填充)
    ans = 0

    for i in range(1, n-1):
        # 长度, 索引
        j = 0 
        # 同时解决"aba"和"abba"型
        # 因为以"#"为中心, 对应"abba"型
        while s[i - j - 1] == s[i + j + 1]:
            j += 1 
        
        if j > ans:
            ans = j 
    
    return ans

"""
充分利用回文串的性质
将回文看做蘑菇(一个圆)
中心 + 半径(回文长度)
(1) 关于中心对称且被半径覆盖(包含/内切关系), 直接使用对称结果
(2) 超出半径的位置, 需要额外更新
线性时间复杂度O(N)
"""
def Manacher_Algorithm(s):
    # 填充后, 单边扩展长度 = 回文长度
    s = "^#" + "#".join(s) + "#$"
    n = len(s)

    # 需要新变量
    # 每个位置为中心, 扩展的半径(回文长度)
    p = [0 for i in range(n)]
    # 当前最远的蘑菇对应的中心c, 最远距离r(不是半径)
    # 半径是r-c
    c, r = 0, 0

    for i in range(1, n-1):
        # 改进点在于, 不需要全部进while
        # 利用一部分对称性, 被r覆盖住的范围直接利用
        # r - i       : 离右边的距离(被r覆盖住对称)
        # p[2 * c - i]: 关于c的对称点的半径
        if i <= r:
            p[i] = min(r - i, p[2 * c - i])
        # p[i]改进了一定结果
        while s[i - p[i] - 1] == s[i + p[i] + 1]:
            p[i] += 1 
        
        # 更新最远覆盖
        if i + p[i] > r:
            c = i 
            r = i + p[i]
     
    return max(p)