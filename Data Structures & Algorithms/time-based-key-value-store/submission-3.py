class TimeMap:
    # hashmap with array for BS - 1 for set, logn for get / mn

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.map[key]
        l, r = 0, len(nums) - 1

        res = (None, "")
        while l <= r:
            mid = (l + r) // 2
            if nums[mid][0] <= timestamp:
                res = nums[mid]
                l = mid + 1
            else:
                r = mid - 1
        
        return res[1]
