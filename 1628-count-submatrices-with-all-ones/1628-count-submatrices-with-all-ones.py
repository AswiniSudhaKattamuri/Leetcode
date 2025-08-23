class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j-1] + 1 if j > 0 else 1
        total = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] > 0:
                    width = dp[i][j]
                    for k in range(i, -1, -1):
                        width = min(width, dp[k][j])
                        if width == 0:
                            break
                        total += width
        return total
