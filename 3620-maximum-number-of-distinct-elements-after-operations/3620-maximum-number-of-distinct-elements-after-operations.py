class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()  
        distinct_count = 0
        next_free = -10**18  
        for num in nums:
            left = num - k  
            right = num + k  
            if next_free < left:
                next_free = left
            if next_free <= right:
                distinct_count += 1
                next_free += 1  
        return distinct_count
