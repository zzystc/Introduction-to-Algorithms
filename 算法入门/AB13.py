n, m = map(int, input().split())

graph = dict((str(i),[]) for i in range(1, n+1))
# print(graph)
# 边数
for i in range(m):
    j, k = input().split()
    graph[j].append(k)
# print(graph)

in_degree = dict((i,0) for i in graph)
# print(in_degree)
# 计算入度
for i in graph: # 遍历键 {'1': ['2'], '2': ['3'], '3': ['4'], '4': ['5'], '5': []}
    for j in graph[i]:
        in_degree[j] += 1
        
lis = [i for i in in_degree if in_degree[i] == 0] # 寻找入度为0
res = []

while lis:
    c = lis.pop()
    res.append(c)
    for i in graph[c]:
        in_degree[i] -=1
        if in_degree[i] == 0:
            lis.append(i)
            
if len(res) == n:
    print(" ".join(res))
else:
    print(-1)