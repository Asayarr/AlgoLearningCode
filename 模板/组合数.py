# 组合数模板
# 两种场景：n 很小用杨辉三角；n 较大且模质数用阶乘+逆元


# 方法一：杨辉三角预处理，适合 n <= 几千
# C[i][j] = 从 i 个里选 j 个
def comb_table(n):
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        C[i][i] = 1
        for j in range(1, i):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C


# 方法二：阶乘 + 费马小定理求逆元，适合 n 较大、模数 p 是质数
# C(n, r) mod p
def comb_mod(n, r, p):
    if r < 0 or r > n:
        return 0
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % p

    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], p - 2, p)      # 费马小定理求逆元
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % p

    return fact[n] * inv_fact[r] % p * inv_fact[n - r] % p


# 方法三：只算单个组合数，用公式 C(n,r) = n*(n-1)*...*(n-r+1) / r!
# 适合 n 小、r 小的情况，不需要取模
def comb_small(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    return res
