class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        nums = candidates
        nums.sort()

        cur = []
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(nums):
                return

            cur.append(nums[i])
            dfs(i + 1, total + nums[i])

            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, total)

        dfs(0, 0)
        return res
