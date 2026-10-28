class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(seen, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                
                curr.append(nums[i])
                seen.add(nums[i])
                dfs(seen, curr)
                curr.pop()
                seen.remove(nums[i])
        
        dfs(set(), [])
        return res