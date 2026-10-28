class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        curr = []
        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(curr))
            
            if openN < n:
                curr.append("(")
                dfs(openN + 1, closedN)
                curr.pop()
            
            if openN > closedN:
                curr.append(")")
                dfs(openN, closedN + 1)
                curr.pop()
        
        dfs(0, 0)
        return res