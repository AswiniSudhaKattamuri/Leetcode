class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cntP=0
        cntN=0
        for i in range(len(nums)):
            if nums[i]>0:
                cntP+=1
            elif nums[i]==0:
                pass
            else :
                cntN+=1
        return max(cntP,cntN)
        