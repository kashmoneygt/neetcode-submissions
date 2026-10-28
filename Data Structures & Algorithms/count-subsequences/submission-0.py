class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j) -> int:
            if j == len(t):
                return 1 # finished matching t
            if i == len(s):
                return 0 # can't match t anymore
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]: # chars match
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)
            