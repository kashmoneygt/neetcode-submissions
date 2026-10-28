class Solution:
    def isValid(self, s: str) -> bool:
        # brute force - n^2 / n
        # stack - n / n
        stack = []
        
        lookup = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        for c in s:
            if c in lookup:
                stack.append(lookup[c])
            elif not stack or c != stack.pop():
                return False
        
        return len(stack) == 0