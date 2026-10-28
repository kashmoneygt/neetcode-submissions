class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = "", float("inf")

        window, countT = {}, {}
        for c in t: countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)

        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if window[c] == countT.get(c, 0):
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if window[s[l]] + 1 == countT.get(s[l], 0):
                    have -= 1
                l += 1
            
        return res if resLen != -1 else ""