from collections import defaultdict


class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        area = defaultdict(int)

        def neighbors(i, j):
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < n and 0 <= c < n:
                    yield (r, c)

        def dfs(i, j, idx):
            # print(i, j, idx)
            area[idx] += 1
            grid[i][j] = idx
            for r, c in neighbors(i, j):
                if grid[r][c] == 1:
                    dfs(r, c, idx)

        idx = 2
        for i in range(n):
            for j in range(n):
                # print(grid)
                if grid[i][j] == 1:
                    # print(i, j)
                    dfs(i, j, idx)
                    idx += 1

        # print(grid)
        if any([c == 0 for row in grid for c in row]):
            res = 0
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 0:
                        close = set()
                        for r, c in neighbors(i, j):
                            close.add(grid[r][c])
                        res = max(res, sum([area[x] for x in close]) + 1)
        else:
            res = n ** 2
        return res