# 双指针模板
# 两种常见形态：左右指针（有序数组）、滑动窗口（子数组）


# 左右指针：有序数组里找两数之和
def two_sum_sorted(a, target):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == target:
            return i, j
        elif s < target:
            i += 1
        else:
            j -= 1
    return None


# 滑动窗口：和 >= target 的最短子数组长度
def shortest_subarray_sum(a, target):
    left = 0
    cur = 0
    ans = float('inf')
    for right in range(len(a)):
        cur += a[right]
        while cur >= target:
            ans = min(ans, right - left + 1)
            cur -= a[left]
            left += 1
    return ans if ans != float('inf') else -1


# 滑动窗口：不含重复字符的最长子串
def longest_unique_substring(s):
    last = {}
    left = 0
    ans = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        ans = max(ans, right - left + 1)
    return ans
