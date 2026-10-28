class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search 2pass - logm + logn AKA log(mn) / 1
        # binary search 1pass - log(mn) / 1
        R, C = len(matrix), len(matrix[0])

        l, r = 0, R * C - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // C, mid % C
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True

        return False