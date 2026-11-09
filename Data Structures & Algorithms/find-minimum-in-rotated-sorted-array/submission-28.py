class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = float("inf")
        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r]: # we are in non-rotated half so min is left of us
                r = m
            else: # we are in rotated half so min is right of us
                l = m + 1
        
        return nums[l]