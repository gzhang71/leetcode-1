class Solution:
    def removeInvalidParentheses(self, s: str) -> [str]:
        # initialize a set with one element
        # set is used here in order to avoid duplicate element
        def is_valid(s):
            counter = 0
            for x in s:
                if x == '(':
                    counter += 1
                elif x == ')':
                    if counter == 0:
                        return False
                    else:
                        counter -= 1
            return counter == 0

        level = {s}
        res = []
        while len(res) == 0:
            new_level = set()
            for l in level:
                if is_valid(l):
                    res.append(l)

                for i in range(len(l)):
                    new_level.add(l[:i] + l[i + 1:])
            level = new_level

        return res