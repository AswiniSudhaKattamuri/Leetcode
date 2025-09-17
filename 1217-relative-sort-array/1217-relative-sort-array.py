class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter

        count = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num] * count[num])
            count.pop(num)

        remaining = sorted(count.elements())
        result.extend(remaining)

        return result
