from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        unique = sorted(freq.keys())
        n = len(unique)
        dp = [0] * n
        dp[0] = unique[0] * freq[unique[0]]
        j = -1
        for i in range(1, n):
            gain = unique[i] * freq[unique[i]]
            while j + 1 < i and unique[i] - unique[j + 1] >= 3:
                j += 1

            if j >= 0:
                gain += dp[j]

            dp[i] = max(dp[i-1], gain)

        return dp[-1]
