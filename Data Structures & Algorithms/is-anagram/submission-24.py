class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        charS = {}
        charT = {}

        for i in range(len(s)):
            charS[s[i]] = charS.get(s[i], 0) + 1
            charT[t[i]] = charT.get(t[i], 0) + 1
        
        return charS == charT
