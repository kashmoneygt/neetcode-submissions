class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = { "(":")", "{":"}", "[":"]" }
        for c in s:
            if c in maps:
                stack.append(maps[c])
            elif not stack or stack.pop() != c:
                return False
            
        return not stack