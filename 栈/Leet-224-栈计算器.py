def calculate(s: str) -> int:
    # 1. 初步替换, 避免一元符号符号影响
    s = s.replace(" ", "").replace("(-", "(0-").replace("(+", "(0+")
            
    # 2. 维护两个栈, 数字栈nums+运算栈ops
    # 连续数字
    nums = []
    nums.append(0)
    # ["(", ")", "+", "-"]
    ops  = []

    i = 0 

    while i < len(s):
        # 遇到加减号应该吧前边全算完
        if s[i] == "(":
            ops.append(s[i])
            i += 1
        # 一直算到匹配的"("
        elif s[i] == ")":
            op = ops.pop()
            while op != "(":
                # pop两个数, 算num1 ? num2
                num2 = nums.pop()
                num1 = nums.pop()
                # 只有["+", "-"]
                if op == "+":
                    nums.append(num1 + num2)
                else:
                    nums.append(num1 - num2)
                op = ops.pop()
            i += 1
        elif s[i] in ["+", "-"]:
            # 把现有栈里的结果计算一下
            while len(ops) > 0 and ops[-1] != "(":
                op = ops.pop()
                # pop两个数, 算num1 ? num2
                num2 = nums.pop()
                num1 = nums.pop()
                # 只有["+", "-"]
                if op == "+":
                    nums.append(num1 + num2)
                else:
                    nums.append(num1 - num2)
            ops.append(s[i])
            i += 1
        # 连续读数字
        else:
            num = 0
            while i < len(s) and s[i] not in ["(", ")", "+", "-"]:
                num = num * 10  + int(s[i])
                i += 1
            print(f"number: {num}")
            nums.append(num)
    
    # 栈内还剩余一些运算(k个)和数(k+1)个, 每次运算后运算和数都少1, 最后0运算+1数
    print(ops)
    print(nums)
    while len(nums) > 0 and len(ops) > 0:
        op = ops.pop()
        # pop两个数, 算num1 ? num2
        num2 = nums.pop()
        num1 = nums.pop()
        # print(f"oper: {num1} {op} {num2}")
        # 只有["+", "-"]
        if op == "+":
            nums.append(num1 + num2)
        else:
            nums.append(num1 - num2)
    
    # print(nums)
    return nums.pop()



s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s=s))


a = [1,2,3,4]
a.pop()
a.pop()
print(a)