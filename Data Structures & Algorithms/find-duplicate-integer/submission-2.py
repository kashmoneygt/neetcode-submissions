class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sorting - nlogn / 1
        # set or array - n / n
        # fast and slow pointers - n / 1

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
                