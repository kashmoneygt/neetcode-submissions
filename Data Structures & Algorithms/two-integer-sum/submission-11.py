class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seenDict:
                return [seenDict[diff], i]

            if num not in seenDict:
                seenDict[num] = i


    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(0, len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #             j += 1
    #         i += 1