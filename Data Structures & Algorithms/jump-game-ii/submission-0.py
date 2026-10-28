class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0  # window representing level / portion of array

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1 # set it directly after the R pointer
            r = farthest # set it to farthest we can jump from cur level
            res += 1

        return res