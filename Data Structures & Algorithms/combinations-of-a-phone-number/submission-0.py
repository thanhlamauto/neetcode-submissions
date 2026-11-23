class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        result = []
        path = []

        def dfs(i):
            if i == len(digits):
                result.append("".join(path.copy()))
                return
            for char in phone[digits[i]]:
                path.append(char)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return result
