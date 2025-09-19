class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,num in enumerate(nums):
            res=target-num
            if res in dic:
                return [dic[res],i]
            dic[num]=i