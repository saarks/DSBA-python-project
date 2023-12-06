def dfs(start):
    visited.append(start)
    for i in range(n):
        if arr[start][i] == 1 and i not in visited:
            dfs(i)
    return len(visited)

n, s = map(int, input().split())
visited = []
arr = []
for i in range(n):
    m = list(map(int, input().split()))
    arr.append(m)
print(dfs(s))