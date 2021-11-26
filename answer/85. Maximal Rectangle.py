class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
                return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        i = 0
        while i < m:
            j = 0
            while j < n:
                if matrix[i][j] == '0':
                    j += 1
                    continue
                j1 = j
                while j1 < n and matrix[i][j1] == '1':
                    i1 = i
                    while i1 < m and all([x == '1' for x in matrix[i1][j: j1 + 1]]):
                        i1 += 1
                    s = (j1 - j + 1) * (i1 - i)
                    ans = max(ans, s)
                    # print(ans, s, i, i1, j, j1)
                    j1 += 1
                j += 1
            i += 1
        return ans