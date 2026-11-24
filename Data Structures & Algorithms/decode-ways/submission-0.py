class Solution:
    def numDecodings(self, s: str) -> int:
        hmap = {"1":"A", "2":"B", "3":"C", "4":"D", "5":"E",
        "6":"F", "7":"G", "8":"H", "9":"I", "10":"J", "11":"K",
        "12":"L", "13":"M", "14":"N", "15":"O", "16":"P", "17":"Q", 
        "18":"R", "19":"S", "20":"T", "21":"U", "22":"V", "23":"W",
        "24":"X", "25":"Y", "26":"Z"}

        n = len(s)

        memo = {}

        def dfs(i):
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            ways = 0
            if s[i] in hmap:
                ways += dfs(i+1)
            if i + 1 < n and s[i:i+2] in hmap:
                ways += dfs(i+2)
            memo[i] = ways
            return ways
        
        return dfs(0)

        
