"""
201. 数字范围按位与

给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。

示例 1：

输入：left = 5, right = 7
输出：4
示例 2：

输入：left = 0, right = 0
输出：0
示例 3：

输入：left = 1, right = 2147483647
输出：0
 
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 公共前缀: 只要left < right, 这个区间内的数一定有公共前缀
        # 二进制比大小, 一定是SSS1XXX > SSS0XXX, 其中"SSS"是公共前缀
        # 设前i位是公共前缀prefix, 从第i+1开始不同(则至少1个是0, &结果是0)
        # 其次剩余的位置都至少1个0, 固定[x, x+1]
        # (1) [S0, S1] => S0 
        # (2) [S1, X0] => X0...0(+1导致1变0并进位) eg: X1...1, [X+1]0...0
        # 
        bits = 0
        # 找前缀
        while left < right:
            left >>= 1
            right >>= 1 
            bits += 1
        
        return left << bits 
    







