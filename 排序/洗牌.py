import random 

# 等概率抽取k个 <=> 均匀洗牌, 取前k个
arr = [1, 2, 3, 4, 5]

# 保证每个位置的选择, 概率都是1/n
for i in range(n - 1, -1, -1):
    # 选择位置i in [0, n - 1] 的选择牌(保证概率是1/n)
    j = random.randint(0, i)
    arr[i], arr[j] = arr[j], arr[i] 



