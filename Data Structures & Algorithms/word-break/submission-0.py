class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if s.startswith(w, i) and dp[i + len(w)]:
                    dp[i] = True

        return dp[0]