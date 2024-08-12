"""
415. 字符串相加

给定两个字符串形式的非负整数 num1 和num2 , 计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库(比如 BigInteger),  也不能直接将输入的字符串转换为整数形式。

 
示例 1: 

输入: num1 = "11", num2 = "123"
输出: "134"
示例 2: 

输入: num1 = "456", num2 = "77"
输出: "533"
示例 3: 

输入: num1 = "0", num2 = "0"
输出: "0"

扩展面试题:

36进制由0-9, a-z, 共36个字符表示。

要求按照加法规则计算出任意两个36进制正整数的和, 如
    1b + 2x = 48  (解释: 47+105=152)

要求: 不允许使用先将36进制数字整体转为10进制, 相加后再转回为36进制的做法
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 进制的基(可以处理任意基)
        base = 10 
        carry = 0

        # 采用合并有序数组的思想, 对齐短位, 后单独处理多的位
        i = len(num1) - 1 
        j = len(num2) - 1 

        ans = ""
        while i >= 0 or j >= 0 or carry > 0:
            a = int(num1[i]) if i >= 0 else 0 
            b = int(num2[j]) if j >= 0 else 0 
            tmp = a + b + carry 
            ans = str(tmp % base) + ans 
            carry = tmp // base
            i -= 1
            j -= 1 

        return ans 