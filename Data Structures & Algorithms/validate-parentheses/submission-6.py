class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren = { '{':'}', '[':']', '(':')' }
        for c in s:
            if c in "{[(":
                stack.append(paren[c])
            elif not stack or c != stack.pop():
                return False

        return not stack