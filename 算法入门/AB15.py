from typing import *

class Solution:
    n, m = map(int, input().split())
    graph = {}
    for i in range(m):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = {v: w}
        else:
            graph[u][v] = w
        if v not in graph:
            graph[v] = {u: w}
        else:
            graph[v][u] = w

    def func():
        visit = {1}
        need_node = {(1,0): graph[1]}
        arri_node_val = {1: 0}
        
        while True:
            need_node1 = {}
            for u in need_node:
                for v in need_node[u]:
                    if v not in arri_node_val:
                        arri_node_val[v] = u[1] + need_node[u][v]
                        need_node1[v, arri_node_val[v]] = graph[v]
                    else:
                        if arri_node_val[v] > u[1] + need_node[u][v]:
                            arri_node_val[v] = u[1] + need_node[u][v]
                            need_node1[(v, arri_node_val[v])] = graph[v]
            if not need_node1:
                break
            else:
                need_node = need_node1
        if n not in arri_node_val:
            print(-1)
        else:
            print(arri_node_val[n])
            
    # func()

test = Solution()
test.func(4, 3,[[1, 2, 5], [2, 3, 3], [3, 1, 3]])