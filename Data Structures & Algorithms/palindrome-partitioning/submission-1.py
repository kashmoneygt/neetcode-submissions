class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        part = [] # current partition
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1) # go to next char not in partition
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
