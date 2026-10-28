class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for l in s:
            if l.isalnum():
                newStr += l.lower()
        return newStr == newStr[::-1]




