"""
172. 阶乘后的零

末尾0的个数

找因子2, 5

令f(x)表示正整数x末尾所含有的“0”的个数，则有：
      当0 < n < 5时，f(n!) = 0;
      当n >= 5时，f(n!) = k + f(k!), 当中 k = n / 5（取整）。

蚂蚁2024.3.23笔试题
给一个数组arr, 有一次运算使得arr[i] += 1 
问算 or 不算乘积末尾最多0的个数

eg: [1, 2, 3, 4]
初始24, 没有0 
4->5, 是30, 有1个0
"""

def N_factorial_zeros(n):
    if n < 5:
        return 0 
    k = n // 5 
    return k + N_factorial_zeros(k)

# 分解2, 5因子
def factor25(n):
    a, b = 0, 0
    
    while n % 2 == 0:
        n /= 2 
        a += 1 
    
    while n % 5 == 0:
        n /= 5 
        b += 1
    
    return a, b


# print(N_factorial_zeros(100))
print(factor25(100))
x, y = 0, 0
for i in range(2, 101):
    a, b = factor25(i)
    x += a 
    y += b 

print(x, y)
print(min(x, y))


def max_zeros(arr: list[int]):
    x_sum, y_sum = 0, 0
    xy = []
    for n in arr:
        a, b = factor25(n)
        xy.append([a, b])
        x_sum += a 
        y_sum += b 
    
    # 初始答案
    ans = min(x_sum, y_sum)

    for i in range(len(arr)):
        a, b = factor25(arr[i] + 1)
        x_sum += a - xy[i][0]
        y_sum += b - xy[i][1]
        if min(x_sum, y_sum) > ans:
            ans = min(x_sum, y_sum) 
        # 恢复
        x_sum -= a - xy[i][0]
        y_sum -= b - xy[i][1]    
    
    print(ans)

max_zeros(arr=[1,2,4,24])

