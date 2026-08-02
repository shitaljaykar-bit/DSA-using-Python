class Solution:

    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        dp = piles[:]  # Base cases for subarray lengths of 1

        # Build DP table for lengths 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(piles[i] - dp[i + 1], piles[j] - dp[i])

        return dp[0] > 0