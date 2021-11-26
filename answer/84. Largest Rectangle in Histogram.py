class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        n = len(heights)
        ans = 0
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                if heights[j] < min_height:
                    min_height = heights[j]
                s = min_height * (j - i + 1)
                ans = max(s, ans)
        return ans