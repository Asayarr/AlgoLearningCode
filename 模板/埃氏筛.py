# 埃氏筛：筛出 1..n 的所有素数
# 复杂度 O(n log log n)
# 思路：从 2 开始，把每个素数的倍数全部划掉，剩下的就是素数

from math import isqrt


def build_primes(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False                  # 0 和 1 不是素数
    for i in range(2, isqrt(n) + 1):
        if is_p[i]:                            # i 是素数，才去划它的倍数
            # 从 i*i 开始划，因为比 i*i 小的倍数已经被更小的素数划过了
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return [i for i in range(2, n + 1) if is_p[i]]


# 用素数表判断一个数是不是素数
# 参数 primes 是 build_primes 筛出来的列表
def is_prime(x, primes):
    if x < 2:
        return False
    for p in primes:
        if p * p > x:                          # 超过 sqrt(x) 就不用再试了
            break
        if x % p == 0:
            return False
    return True


# 使用示例：
#   要判断的数最大是 10^7，sqrt(10^7) 约 3163，所以筛到 4000 就够
#   PRIMES = build_primes(4000)
#   print(is_prime(97, PRIMES))
#
# 注意：
#   1. 只判断一两个数时，直接试除到 sqrt(x) 就行，不用筛表
#   2. 要判断很多次（上万次），才先筛素数表
