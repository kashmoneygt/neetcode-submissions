class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = n

        n = 1
        n_1 = 1
        
        for _ in range(stairs - 1):
            temp = n_1
            n_1 = n_1 + n
            n = temp
        
        return n_1


