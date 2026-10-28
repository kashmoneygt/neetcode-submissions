class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [ [float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1) ]

        # set # of insert operations needed when i is empty and j is nonempty
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # set # of delete operations needed when i is nonempty and j is empty
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1] # no ops needed
                else:
                    dp[i][j] = 1 + min(   # 1 op needed
                        dp[i][j + 1],     # insert
                        dp[i + 1][j],     # delete
                        dp[i + 1][j + 1]  # replace
                    )
        
        return dp[0][0]
