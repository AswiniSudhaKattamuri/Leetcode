class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalDrunk = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            full = 1
            totalDrunk += full
            empty += full  
            numExchange += 1  
        return totalDrunk
