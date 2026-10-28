class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force - merge two arrays - (n+m)log(n+m) / n+m
        # two pointer - n+m / 1
        # BS with get_kth() - log(n+m) / log(n+m)
        # BS optimal (Al<=Br and Bl<=Ar) - log(min(n,m)) / 1
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A): A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                return (
                    min(Aright, Bright)
                    if total % 2
                    else (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                )
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

