class Solution:
    def addOperators(self, num: str, target: int) -> [str]:
        n = len(num)
        res = []

        def dfs(num, curr, curr_value, status):
            m = len(num)
            if m == 0 and curr_value == target:
                res.append(status)
            if m == 0:
                return
            for j in range(1, m + 1):
                new_curr = num[:j]
                if j == 1 or new_curr[0] != '0' and len(new_curr) > 1:
                    dfs(num[j:], int(new_curr), curr_value + int(new_curr), status + '+' + new_curr)
                    dfs(num[j:], -int(new_curr), curr_value - int(new_curr), status + '-' + new_curr)
                    dfs(num[j:], curr * int(new_curr), curr_value - curr + curr * int(new_curr),
                        status + '*' + new_curr)

        for i in range(1, n + 1):
            if i == 1 or num[0] != '0' and i > 1:
                dfs(num[i:], int(num[:i]), int(num[:i]), num[:i])
        return res