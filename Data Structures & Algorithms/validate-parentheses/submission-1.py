class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        lookup = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        for c in s:
            if c in ['{', '(', '[']:
                stack.append(lookup[c])
            elif not stack or c != stack.pop():
                return False
        
        return len(stack) == 0