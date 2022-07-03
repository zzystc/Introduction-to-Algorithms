#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回最小的花费代价使得这n户人家连接起来
# @param n int整型 n户人家的村庄
# @param m int整型 m条路
# @param cost int整型二维数组 一维3个参数，表示连接1个村庄到另外1个村庄的花费的代价
# @return int整型
#
from typing import *

class Union:
    def __init__(self, n: int):
        self.parent = [0 for _ in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        self.count = n
        for i in range(n + 1):
            self.parent[i] = i
            self.rank[i] = 1
            
    def find(self, x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])
    
    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi == yi:
            return
        if self.rank[xi] > self.rank[yi]:
            self.parent[yi] = xi
            self.rank[xi] += self.rank[yi]
        else:
            self.parent[xi] = yi
            self.rank[yi] += self.rank[xi]
        self.count -= 1
        
    def connection(self, x ,y):
        xi ,yi = self.find(x), self.find(y)
        return xi == yi
        
    def count(self):
        return self.count          
    
class Solution:
    def miniSpanningTree(self , n: int, m: int, cost: List[List[int]]) -> int:
        # write code here
        union = Union(n)
        cost.sort(key = lambda x: x[2])
        res = 0
        for a, b, w in cost:
            if union.connection(a, b):
                continue
            res += w
            union.union(a, b)
        return res
        
test = Solution()
print(test.miniSpanningTree(3,3,[[1,3,3],[1,2,1],[2,3,1]]))