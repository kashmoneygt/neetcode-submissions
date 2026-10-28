class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        def backtrack(i, total):
            if i == len(nums) or total > target:
                return
            
            if total == target:
                res.append(combo.copy())
                return
            
            combo.append(nums[i])
            backtrack(i, total + nums[i])

            combo.pop()
            backtrack(i + 1, total)



        backtrack(0, 0)
        return res
