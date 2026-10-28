class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"{":"}", "[":"]", "(":")"}
        stack = []

        for c in s:
            if c in mp:
                stack.append(mp[c])
            elif not stack or stack.pop() != c:
                return False

        return not stack
