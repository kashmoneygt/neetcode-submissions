class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax = 0, 0

        for i, c in enumerate(s):
            if c == "(":
                openMin += 1
                openMax += 1
            elif c == ")":
                openMin -= 1
                openMax -= 1
            else:
                openMin -= 1
                openMax += 1

            if openMin < 0:
                openMin = 0
            if openMax < 0:
                return False

        return openMin <= 0 <= openMax