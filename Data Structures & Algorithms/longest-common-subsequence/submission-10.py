class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LCS = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        # LCS[len(text1)][len(text2)] = 1

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    LCS[i][j] = 1 + LCS[i + 1][j + 1]
                else:
                    LCS[i][j] = max(LCS[i + 1][j], LCS[i][j + 1])

        return LCS[0][0]