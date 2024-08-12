"""
素数专题

素数定义:
    在大于1的自然数中, 除了1和它本身不再有其他因数的自然数

(1) 素数筛
    朴素筛法, 判断单个素数的复杂度O(sqrt(N))

(2) 找全部的素因子
对于一个N, 找素因子的复杂度是O(sqrt(N))
而前N个数里边素数个数为N/lnN
则前sqrt(N)里边只有sqrt(N)/ln(sqrt(N))个素数

算数基本定理:
任何自然数N>1, 可以唯一分解为有限个素数乘积
    N = P1^a1*P2^a2...*Pn^an



"""

# 快速幂
def quick_pow(x, n):
    ans = 1 
    while n:
        if n & 1:
            ans = ans * x 
        x = x * x 
        n >>= 1
    
    print(ans)

def isPrime_basic(n: int):
    # 除了2的偶数都不是素数
    if n < 2 or (n != 2 and n % 2 == 0):
        return False 
    
    # 不用从2开始了
    for i in range(3, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            return False 
    return True 


quick_pow(3, 10)

print(pow(5, 0.5))

"""
204. 计数质数
"""
# 埃氏筛, 标记素数的倍数, 从x*x开始, 
# 所有 < 
# 时间复杂度: O(nloglogn) 约等于 O(n)
def countPrimes(n: int) -> int:
        
        isPrime = [1] * n 
        ans = 0

        for i in range(2, n):
            if isPrime[i]:
                ans += 1 
                for j in range(i * i, n, i):
                    isPrime[j] = 0
        
        return ans

print(countPrimes(n=7))

"""

方法三：线性筛
此方法不属于面试范围范畴，本节只做简单讲解。

埃氏筛其实还是存在冗余的标记操作，比如对于 45 这个数，它会同时被 3,5 两个数标记为合数，因此我们优化的目标是让每个合数只被标记一次，这样时间复杂度即能保证为 O(n)。

需要多维护一个primes数组存当前素数集合

区别于[埃氏筛], [标记过程]对每一个整数(不只素数)都进行, 不再标记倍数x*x, x*(x+1)...
只标记y in primes与x相乘的数, 当 x % y = 0时结束标记

核心:
若x可以被某个primes[i]整除, 则对于合数x*primes[j](j>i), 它会在之后遇到(x/primes[i])*primes[j]时被标记, 保证了每个合数只会被其[最小的素因子]筛去, 即只被标记一次

"""

def count_primes_linear_sieve(n):
    isPrime = [1] * n 
    primes = []

    for x in range(2, n):
        if isPrime[x]:
            primes.append(x)
        
        for y in primes:
            if x * y > n - 1:
                break
            isPrime[x * y] = 0
            # 可以被后边的数筛去
            if x % y == 0:
                break

    print(primes)
    return len(primes) 

count_primes_linear_sieve(23)


"""
素因数分解
"""

def prime_factor(n):
    ans = []
    for i in range(2, int(pow(n, 0.5) + 1)):
        if n % i  == 0:
            # 因子个数, 除到不能再除
            k = 0

            while n % i == 0:
                n /= i 
                k += 1 
            ans.append([i, k])
    if n > 1:
        ans.append([n, 1])
    
    print(ans)

prime_factor(100)



