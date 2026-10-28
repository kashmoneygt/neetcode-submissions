class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        mp = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []

        combo = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(combo))
                return
            
            for c in mp[digits[i]]:
                combo.append(c)
                dfs(i + 1)
                combo.pop()
        
        dfs(0)
        return res

