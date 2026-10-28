class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if x == 0: return 0  # 0^n = 0
            if n == 0: return 1  # x^0 = 1

            # n = 4 -> compute n = 2 and multiply res with itself 
            # optimize: if we pass in x*x, don't need to mult res
            res = helper(x * x, n // 2)

            # handle odd case (n = 5) -> multiply with x
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res # handle neg exponent