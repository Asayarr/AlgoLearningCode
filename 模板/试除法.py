from math import isqrt

def is_prime(x):
    if x < 2:
        return False
    for d in range(2, isqrt(x) + 1):   # 只试到 √x
        if x % d == 0:
            return False
    return True