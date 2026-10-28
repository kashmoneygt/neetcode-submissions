class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}
        
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0
            if (i, open) in cache:
                return cache[(i, open)]
            
            if s[i] == "(":
                res = dfs(i + 1, open + 1)
            elif s[i] == ")":
                res = dfs(i + 1, open - 1)
            else:
                res = dfs(i + 1, open - 1) or dfs(i + 1, open) or dfs(i + 1, open + 1)
            
            cache[(i, open)] = res
            return res

        return dfs(0, 0)

