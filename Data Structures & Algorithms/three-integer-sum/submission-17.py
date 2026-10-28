class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort then brute force - n^3 / m (# triplets)
        # sort then hashmap - n^2 / n
        # sort then two pointer - n^2 / 1
        nums.sort()

        res = set()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return [[i,j,k] for i,j,k in res]