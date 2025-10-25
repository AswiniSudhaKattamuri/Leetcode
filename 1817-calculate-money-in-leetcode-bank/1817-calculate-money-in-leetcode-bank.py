class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        total = 28 * weeks + 7 * (weeks - 1) * weeks // 2
        total += (weeks + 1 + weeks + days) * days // 2
        return total
