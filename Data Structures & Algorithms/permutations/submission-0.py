class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])
        res = []

        for permutation in permutations:
            # Put nums[0] in every position of the permutation
            for i in range(len(permutation) + 1):
                copy = permutation.copy()
                copy.insert(i, nums[0])
                res.append(copy)

        return res