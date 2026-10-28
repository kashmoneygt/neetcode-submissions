class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            # even
            l, r = i, i + 1
            while l < r and l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1


            # odd
            l, r = i, i
            while l <= r and l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]

                l -= 1
                r += 1

        return res