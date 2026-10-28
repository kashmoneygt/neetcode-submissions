class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top-down memoization
        cache = {} # (i, j) -> whether string s and pattern p match up to i and j

        def dfs(i, j) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p): # both are out of bounds
                return True
            if j >= len(p):
                # if we finished going thru pattern but i isn't matched yet
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*": # next char in pattern is *
                cache[(i, j)] = (
                    dfs(i, j + 2) or          # don't use *
                    (match and dfs(i + 1, j)) # use * if there's a match
                )
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False    
            return False # s and p don't match at i and j
        
        return dfs(0, 0)