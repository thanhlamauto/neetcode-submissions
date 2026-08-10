class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        freq = dict()

        for r in range(len(s)):
            c = s[r]
            freq[c] = freq.get(c, 0) + 1

            while (r - l + 1) - max(freq.values()) > k:
                d = s[l]
                freq[d] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans
