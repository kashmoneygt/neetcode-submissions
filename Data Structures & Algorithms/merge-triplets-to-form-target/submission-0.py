class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set() # track which positions we're able to match (values can only be 0, 1, 2)

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # ignore triplet

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i) # found a position we can match at from this triplet

        return len(good) == 3
