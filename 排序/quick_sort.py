"""
快排模板: pivot
选择一个基准pivot, 分成两段
x < pivot > y
low, high重合则进入递归

在未排序的数组中找一个基准pivot(如最左边), 将所有比pivot小的数放在左边, 大的数放在右边, 然后对左右两边重复进行, 直到完成全部排序

递归参数: low-high边界
终止条件: low>=high

单次过程:
(1) low->指针i, high->指针j
(2) (先)移动指针j, 直到有小于pivot的/遇到指针i
(3) (再)移动指针i, 直到有大于pivot的/遇到指针j 
(4) i, j未相遇, 交换i, j的数
(5) 重复(1-4)直到i >= j
(6) 交换pivot与arr[j]的值, 本次局部排序完成

方法一：填坑法
1.利用分化函数求第一个基准元素
2.递归调用快排
主要是分化函数partition的实现
分化函数步骤：
1.第一个位置作为基准，位置为初始坑
2.先从右边元素，找到小于基准的元素，填入坑中，更新坑位置，找到后转3
3.从左边找到大于基准的元素，填入坑中，更新坑位置；2,3循环直到left = right
4.最后的坑填入基准元素。

方法二：指针交换法
与填坑法相比，只有分化函数不同，分化函数中的元素交换次数少，更简单
交换思想：左边大于基准的元素和右边小于基准的元素交换
分化函数步骤：
1.交换
2.当left和right指针重合之时，交换pivot元素和left与right重合点的元素

！！！一定要从基准的对面开始比较
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/vict_wang/article/details/83118746

归并模板

"""

# [low, high]
# eg: arr = [4,3,2,1], low = 0, high = 3
def quick_sort(arr, low, high):
    if low >= high:
        return 
    
    print(low, high)
    # 此时low也是这个位置, 相当于空出了一个坑
    pivot = arr[low]
    i, j = low, high
    
    while i < j:
        while i < j and arr[j] >= pivot:
            j -= 1 

        while i < j and arr[i] <= pivot:
            i += 1 

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    print("i: ", i)
    print("j: ", j)
    # 最后移动基准, 此时i, j一定相同
    arr[low], arr[i] = arr[i], arr[low]
    # 此时左边全是小的, 右边全是大的
    quick_sort(arr, low, i - 1)
    quick_sort(arr, i + 1, high)

arr = [6,5,4,3,2,1] + [6,5,4,3,2,1]

quick_sort(arr, 0, 11)
print(arr)


