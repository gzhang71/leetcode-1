# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        curr = root
        last = Node(0)
        head = last
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            last.right = curr
            curr.left = last
            last = curr
            curr = curr.right

        curr = head.right
        last.right = curr
        curr.left = last
        return curr
