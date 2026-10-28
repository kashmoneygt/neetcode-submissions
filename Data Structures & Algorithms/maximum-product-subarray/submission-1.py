class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            oldCurMax = curMax

            # To include n in streak, pick max of:
            curMax = max(curMax * n, # max * n
                curMin * n,          # min * n (neg*neg=pos)
                n)                   # n by itself (restart)

            # min() same as above
            curMin = min(oldCurMax * n, curMin * n, n)

            res = max(res, curMax)

        return res