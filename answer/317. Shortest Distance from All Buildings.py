from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        hit = [[0] * n for _ in range(m)]
        distsum = [[0] * n for _ in range(m)]
        buildings = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        def neighbors(i, j):
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    yield x, y

        def bfs(queue):
            while queue:
                # print(queue)
                i, j, dist = queue.popleft()
                for x, y in neighbors(i, j):
                    if not visited[x][y] and not grid[x][y]:
                        queue.append((x, y, dist + 1))
                        visited[x][y] = True
                        hit[x][y] += 1
                        distsum[x][y] += dist + 1

        for b in buildings:
            visited = [[False] * n for _ in range(m)]
            visited[b[0]][b[1]] = True
            queue = deque([(b[0], b[1], 0)])
            bfs(queue)
            # print(hit)
            # print(distsum)
        # print(hit)
        # print(distsum)
        res = len(buildings) * (m + n)
        if not any([x == len(buildings) for row in hit for x in row]):
            return -1

        for i in range(m):
            for j in range(n):
                if hit[i][j] == len(buildings) and distsum[i][j] < res:
                    res = distsum[i][j]

        return res