class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = {}
            for num in window:
                freq[num] = freq.get(num, 0) + 1

            sorted_items = sorted(freq.items(), key=lambda y: (-y[1], -y[0]))

            total = 0
            for val, count in sorted_items[:x]:
                total += val * count

            result.append(total)

        return result
