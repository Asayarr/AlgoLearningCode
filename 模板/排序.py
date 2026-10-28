# 排序模板


def demo_sort():
    a = [3, 1, 2]

    a.sort()                    # 原地排序，返回 None
    b = sorted(a)               # 返回新列表，a 不变
    a.sort(reverse=True)        # 降序

    students = [('Tom', 90), ('Amy', 85), ('Bob', 95)]

    students.sort(key=lambda x: x[1])          # 按第二项升序
    students.sort(key=lambda x: -x[1])         # 按第二项降序

    # 多关键字：先按分数降序，再按名字升序
    students.sort(key=lambda x: (-x[1], x[0]))

    # 元组默认排序：从左到右逐位比较
    c = [(3, 'b'), (1, 'c'), (3, 'a')]
    c.sort()                    # [(1, 'c'), (3, 'a'), (3, 'b')]

    return a, b, students, c


# 注意：
# 1. a.sort() 返回 None，别写 a = a.sort()
# 2. 多关键字降序用 -x 只对数字有效；字符串要先升序再整体 reverse，或者多趟排序
# 3. 需要稳定排序时，sorted / sort 都是稳定的
