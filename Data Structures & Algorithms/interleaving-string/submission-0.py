class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and s1[i - 1] == s3[i+j - 1] and dp[i-1][j]:
                    dp[i][j] = True
                if j > 0 and s2[j - 1] == s3[i + j - 1] and dp[i][j-1]:
                    dp[i][j] = True
        
        return dp[m][n]