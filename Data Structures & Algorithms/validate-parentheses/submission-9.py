class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "[":"]",
            "(":")",
            "{":"}",
        }
        stack = []

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            elif not stack or stack.pop() != c:
                return False
        
        return not stack
