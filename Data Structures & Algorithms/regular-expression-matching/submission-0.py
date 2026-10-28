class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top-down memoization
        dp = {} # (i, j) -> whether string s and pattern p match up to i and j

        def dfs(i, j) -> bool:
            if i >= len(s) and j >= len(p): # both are out of bounds
                return True
            if j >= len(p):
                # if we finished going thru pattern but i isn't matched yet
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*": # next char in pattern is *
                return (
                    dfs(i, j + 2) or          # don't use *
                    (match and dfs(i + 1, j)) # use * if there's a match
                )
            
            if match:
                return dfs(i + 1, j + 1)
            
            return False # s and p don't match at i and j
        
        return dfs(0, 0)