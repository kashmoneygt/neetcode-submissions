class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0]) # right starts at len() rather than len() - 1
        top, bottom = 0, len(matrix)    # same with bot, to not specify -1 in range()

        while left < right and top < bottom:
            # Process top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Process right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check if pointers have crossed
            # Happens with single-row or single-col matrix like [1,2,3]
            if not (left < right and top < bottom):
                break

            # Process bottom row
            for i in range(right - 1, left - 1, -1): # left non-inclusive
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Process left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
