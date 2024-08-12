# 11011 -> 翻转0->1 return 5
# 001   -> 翻转1->0 return 3
s = [1,1,0,1,1]
s = [0,0,1] + [1,1,0,1,1]
n = len(s)

# left1[i], 当s[i]===0时, [:i]连续1的个数
# right[i], 当s[i]===0, [i+1:]连续1的个数
# 这样max(left1[i]+right1[i])+1表示把位置i从0->1后连续的1长度
left1 = [0 for _ in range(n)]
right1 = [0 for _ in range(n)]
left0 = [0 for _ in range(n)]
right0 = [0 for _ in range(n)]

for i in range(1, n):
    if s[i - 1] == 1:
        left1[i] = left1[i - 1] + 1
        left0[i] = 0
    else:
        left0[i] = left0[i - 1] + 1
        left1[i] = 0

for i in range(n - 2, -1, -1):
    if s[i + 1] == 1:
        right1[i] = right1[i + 1] + 1
        right0[i] = 0
    else:
        right0[i] = right0[i - 1] + 1
        right1[i] = 0

print(left1)
print(right1)     
print(left0)
print(right0)

ans = 1
for i in range(n):
    # 0 -> 1
    if s[i] == 0:
        ans = max(ans, 1 + left1[i] + right1[i])
    else:
        ans = max(ans, 1 + left0[i] + right0[i])

print(ans)