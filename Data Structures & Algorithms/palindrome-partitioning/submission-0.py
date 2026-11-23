class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(start):
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start, len(s)):
                if is_pal(start, end):
                    path.append(s[start:end+1])
                    dfs(end + 1)
                    path.pop()
        
        dfs(0)
        return result
        


