class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashset or array - n / 1
        if len(s) != len(t): return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for c in count:
            if c != 0: return False

        return True