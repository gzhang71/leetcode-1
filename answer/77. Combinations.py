class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, k + 1)) + [n + 1]
        res = []
        i = 0
        while i < k:
            print(nums)
            res.append(nums[:k])
            i = 0

            while i < k and nums[i + 1] == nums[i] + 1:
                nums[i] = i + 1
                i += 1
            nums[i] += 1
        return res