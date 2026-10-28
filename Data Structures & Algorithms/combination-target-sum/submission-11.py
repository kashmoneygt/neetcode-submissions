class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        curr = []
        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(nums):
                return
            
            # choose nums[i]
            curr.append(nums[i])
            dfs(i, total + nums[i])

            # don't choose nums[i]
            curr.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
        