class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(seen, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if nums[i] in seen:
                    continue

                cur.append(nums[i])
                seen.add(nums[i])
                dfs(seen, cur)
                cur.pop()
                seen.remove(nums[i])
            
        dfs(set(), [])
        return res