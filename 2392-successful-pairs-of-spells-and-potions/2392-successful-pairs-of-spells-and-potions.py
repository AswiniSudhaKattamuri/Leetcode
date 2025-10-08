from bisect import bisect_left
import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  
        m = len(potions)
        res = []
        for spell in spells:
            needed = math.ceil(success / spell)
            idx = bisect_left(potions, needed)
            res.append(m - idx)
        return res
