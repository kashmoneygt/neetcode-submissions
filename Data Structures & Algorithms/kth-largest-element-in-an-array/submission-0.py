class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l, r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]
            if p < k:
                return quickSelect(p + 1, r)
            elif p > k:
                return quickSelect(l, p - 1)
            else:
                return nums[p]
    
        return quickSelect(0, len(nums) - 1)