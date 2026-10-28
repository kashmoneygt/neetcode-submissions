class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sorting - nlogn / 1
        # set or array - n / n
        # negative marking - make each num neg - n / 1
        # fast and slow pointers (floyd) - identify beginning of cycle - n / 1

        slow, fast = 0, 0
        while True:
            slow = nums[slow]       # 0 1 2 3 2 3 2
            fast = nums[nums[fast]] # 0 2 2
            if slow == fast:
                break

        # slow is at 2
        slow2 = 0
        while True:
            slow = nums[slow]   # 3 2
            slow2 = nums[slow2] # 1 2
            if slow == slow2:
                return slow
