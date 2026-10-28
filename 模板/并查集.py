# 并查集（Union-Find）
# 用途：判断两个元素是否连通、合并集合、找环
# 关键：路径压缩 + 按秩合并，两个一起用接近 O(1)


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # 路径压缩：把查找路径上的点直接挂到根节点
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False          # 已经在同一集合，合并失败（可用于判环）
        # 按秩合并：矮树挂到高树下面，避免树退化成链
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

    def same(self, a, b):
        return self.find(a) == self.find(b)


# 使用示例：
# dsu = DSU(n)
# for 每条边 (u, v):
#     if not dsu.union(u, v):
#         说明 u 和 v 已经连通，这条边会形成环
