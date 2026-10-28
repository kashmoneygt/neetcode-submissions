class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = { '{':'}', '[':']', '(':')' }
        stack = []

        for c in s:
            if c in openToClose:
                stack.append(openToClose[c])
            else:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0