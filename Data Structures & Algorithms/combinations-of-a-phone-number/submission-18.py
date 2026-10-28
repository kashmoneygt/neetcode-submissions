class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []

        cur = []
        def dfs(i):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return
            
            for letter in phoneMap[digits[i]]:
                cur.append(letter)
                dfs(i + 1)
                cur.pop()
        
        if digits:
            dfs(0)
        
        return res

