from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        mn = min(nums)
        mx = max(nums)
        low = max(0, mn - k)
        high = mx + k
        size = high + 1

        freq = [0] * (size)
        for x in nums:
            freq[x] += 1

 
        pref = [0] * (size)
        running = 0
        for i in range(size):
            running += freq[i]
            pref[i] = running

        ans = 1
      
        for v in range(low, high + 1):
            left = max(0, v - k)
            right = min(high, v + k)
            total_in_range = pref[right] - (pref[left - 1] if left - 1 >= 0 else 0)
            equals_v = freq[v] if v < len(freq) else 0
            can_convert = min(numOperations, total_in_range - equals_v)
            possible_freq = equals_v + can_convert
            if possible_freq > ans:
                ans = possible_freq

    
            if ans == n:
                return n

        return min(ans, n)
