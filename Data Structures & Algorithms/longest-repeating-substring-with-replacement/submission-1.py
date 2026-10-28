class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count ={} # hashmap to count characters
        res = 0

        l = 0

        for r in range(len(s)):
            # for the character at position r, we increment the count of it
            # otherwise return a default value of zero
            count[s[r]] = 1 + count.get(s[r], 0)

            # while the length of the window minus the count of the most frequemt character
            # this represents the number of replacement we would need to do
            # if the replacements is greater than allowed, K, 
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            # get the size of the window
            res = max(res, r-l+1)
        return res


# Time Complexity: O(1)
        