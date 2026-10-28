class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0


        for r in range(len(s)):
            while s[r] in charSet: # if the character is in the set so duplicate, then update window
                charSet.remove(s[l]) # remove the left most character
                l+=1 # update pointer by 1
            charSet.add(s[r]) # now you can add the value that was at right pointer to SET since we removed the character duplicate in previous window
            res = max(res, r-l+1)
        return res


# loop the string with a right-pointer and
# if the right-pointer comes across another value that is within the SET
# then remove the value at the left-most pointer from the SET
# and increment the left-pointer by one
# then add the character at the right-pointer to the SET
# calculate the length of the substring (r-1+1) return the max

