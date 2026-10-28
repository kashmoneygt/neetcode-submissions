class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window, maxf = {}, 0

        l, res = 0, 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] > maxf:
                maxf = window[s[r]]

            while (r - l + 1) - maxf > k:
                window[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            
        return res
