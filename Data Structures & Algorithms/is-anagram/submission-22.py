class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        if sorted(s) != sorted(t):
            return False
        return True