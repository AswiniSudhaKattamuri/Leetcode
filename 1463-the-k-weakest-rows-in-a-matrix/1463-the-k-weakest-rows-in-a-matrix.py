class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [(sum(row), i) for i, row in enumerate(mat)]
        soldiers.sort()
        return [i for _, i in soldiers[:k]]
