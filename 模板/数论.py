# 数论模板：gcd / lcm / 快速幂 / 质因数分解
# 这些是蓝桥杯填空题和数论题的基础工具


# 最大公约数（辗转相除法）
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a // gcd(a, b) * b


# 快速幂：计算 a^n mod m
# 复杂度 O(log n)，n 很大时也必须用这个
def fast_pow(a, n, m):
    res = 1
    a %= m
    while n > 0:
        if n & 1:                 # n 的当前最低位是 1，就乘进答案
            res = res * a % m
        a = a * a % m             # a 平方
        n >>= 1                   # n 右移一位
    return res


# 质因数分解：返回 [(质因子, 指数), ...]
# 例：360 -> [(2,3), (3,2), (5,1)]
def factorize(x):
    res = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            cnt = 0
            while x % d == 0:
                x //= d
                cnt += 1
            res.append((d, cnt))
        d += 1
    if x > 1:                     # 剩下的一定是质数
        res.append((x, 1))
    return res


# 由质因数分解推约数个数
# 公式：(e1+1) * (e2+1) * ...
def divisor_count(x):
    cnt = 1
    for _, e in factorize(x):
        cnt *= (e + 1)
    return cnt


# 由质因数分解推约数之和
# 公式：对每个 (p, e)，累乘 (p^(e+1)-1)/(p-1)
def divisor_sum(x):
    s = 1
    for p, e in factorize(x):
        s *= (p ** (e + 1) - 1) // (p - 1)
    return s
