class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        nums = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7": "pqrs", "8":"tuv", "9":"wxyz"}

        def dfs(i, cur):
            if i == len(digits):
                res.append(cur)
                return
            
            for c in nums[digits[i]]:
                dfs(i + 1, cur + c)
            
        if digits:
            dfs(0, "")
        return res