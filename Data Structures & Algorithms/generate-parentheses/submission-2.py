class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        curr = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                stack.append("".join(curr))
                return
            
            if openN < n:
                curr.append("(")
                backtrack(openN + 1, closeN)
                curr.pop()
            
            if closeN < openN:
                curr.append(")")
                backtrack(openN, closeN + 1)
                curr.pop()

        backtrack(0, 0)
        return stack