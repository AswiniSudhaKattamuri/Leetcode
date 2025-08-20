class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        startRow, startCol = startPos
        homeRow, homeCol = homePos
        total = 0

     
        if startRow < homeRow:
            for r in range(startRow + 1, homeRow + 1):
                total += rowCosts[r]
        else:
            for r in range(startRow - 1, homeRow - 1, -1):
                total += rowCosts[r]

        if startCol < homeCol:
            for c in range(startCol + 1, homeCol + 1):
                total += colCosts[c]
        else:
            for c in range(startCol - 1, homeCol - 1, -1):
                total += colCosts[c]

        return total
