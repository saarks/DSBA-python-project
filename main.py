def dfs(v):
    visited.append(v)

    for i in range(1, n + 1):  # Изменение диапазона для учета нумерации с единицы
        if graph[v-1][i-1] == 1 and i not in visited:  # Изменение индексов для учета нумерации с единицы
            dfs(i)


n, s = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = []
dfs(s)

print(len(visited))