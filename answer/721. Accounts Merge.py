from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        graph = defaultdict(set)
        visited = {}
        email_to_account = {}

        def dfs(email, res):
            for e in graph[email]:
                if not visited[e]:
                    visited[e] = True
                    res.append(e)
                    dfs(e, res)
            return res

        for a in accounts:
            default_email = a[1]
            for email in a[1:]:
                graph[email].add(default_email)
                graph[default_email].add(email)
                email_to_account[email] = a[0]
                visited[email] = False

        # print(graph)
        res = []
        for email, account in email_to_account.items():
            node = []
            if not visited[email]:
                dfs(email, node)
                res.append([account] + sorted(node))
        return res