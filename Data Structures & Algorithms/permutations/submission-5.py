class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])
        res = []

        for permutation in permutations:
            for i in range(len(permutation) + 1):
                copy = permutation.copy()
                copy.insert(i, nums[0])
                res.append(copy)
        
        return res