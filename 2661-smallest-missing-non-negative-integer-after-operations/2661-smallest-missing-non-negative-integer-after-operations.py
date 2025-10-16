class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter
        
        
        rem_count = Counter(((num % value) + value) % value for num in nums)
        i = 0
        while True:
            rem = i % value
            if rem_count[rem] > 0:
                rem_count[rem] -= 1 
                i += 1
            else:
                return i  
