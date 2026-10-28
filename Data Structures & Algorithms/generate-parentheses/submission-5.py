class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        cur = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(cur))
                return
            
            if openN < n:
                cur.append("(")
                backtrack(openN + 1, closedN)
                cur.pop()
            
            if closedN < openN:
                cur.append(")")
                backtrack(openN, closedN + 1)
                cur.pop()
        
        backtrack(0, 0)
        return res