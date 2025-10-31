class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        result = []
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] == 2:
                result.append(num)
        
        return result
