class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0 # i-2 house
        rob2 = 0 # i-1 house

        for n in nums:
            temp = max(n + rob1 , rob2)
            rob1 = rob2 # now becomes i-1 house
            rob2 = temp # now becomes i house

        return rob2 # equal to last, max from entire neighborhood