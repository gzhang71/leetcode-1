class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        n = len(nums)
        a, b = 0, n - 1
        ans = 0
        while a <= b:
            m = (a + b) // 2
            if m == n - 1:
                break
            if nums[m] < nums[m + 1]:
                ans = m + 1
                a = m + 1
            else:
                ans = m
                b = m - 1

        return ans