class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            oldCurMax = curMax
            
            # To include n in streak, pick max of (1), max*n,
            # (2) min*n (neg*neg=pos), or (3) n by itself (restart)
            curMax = max(curMax * n, curMin * n, n)
            
            # min() same as above but use original value of curMax
            curMin = min(oldCurMax * n, curMin * n, n)

            res = max(res, curMax)

        return res
