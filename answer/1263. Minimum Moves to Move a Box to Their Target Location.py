from collections import deque


class Solution:
    def minPushBox(self, grid: [[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    person = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)

        def neighbors(i, j):
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                yield r, c

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'

        def a_to_b(a, b, box):
            queue = deque([a])
            v = []
            while queue:
                # print(queue)
                a = queue.popleft()
                if a == b:
                    return True
                for i, j in neighbors(a[0], a[1]):
                    if valid(i, j) and (i, j) not in v and (i, j) != box:
                        v.append((i, j))
                        queue.append((i, j))

            return False

        queue = deque([(0, box, person)])
        visited = []
        while queue:
            # print(visited, queue)
            dist, box, person = queue.popleft()
            if box == target:
                return dist
            b_coord = [(box[0] + 1, box[1]), (box[0] - 1, box[1]), (box[0], box[1] + 1), (box[0], box[1] - 1)]
            p_coord = [(box[0] - 1, box[1]), (box[0] + 1, box[1]), (box[0], box[1] - 1), (box[0], box[1] + 1)]

            for new_box, new_person in zip(b_coord, p_coord):
                if valid(*new_box) and new_box + box not in visited:
                    # print(a_to_b(person, new_person, box), person, new_person, box)
                    if valid(*new_person) and a_to_b(person, new_person, box):
                        visited.append(new_box + box)
                        queue.append([dist + 1, new_box, box])

        return -1




