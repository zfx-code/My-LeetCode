"""
18. 四数之和

给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
"""

def fourSum( nums: list[int], target: int):
    n = len(nums)

    nums.sort()

    ans = []
    for a in range(n - 3):

        if a > 0 and nums[a] == nums[a - 1]:
            continue
        if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target: 
            break
        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue

            if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target: 
                break
            
            # 找索引c, d 
            c = b + 1 
            d = n - 1 

            while c < d:
                if nums[a] + nums[b] + nums[c] + nums[d] == target:
                    ans.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1 
                    d -= 1
                    while c < d and nums[c] == nums[c - 1]:
                        c += 1 
                    while c < d and nums[d] == nums[d + 1]:
                        d -= 1 
                elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                    c += 1 
                else:
                    d -= 1 

    return ans

nums = [-2,-1,-1,1,1,2,2]
target = 0
print(fourSum(nums, target))

