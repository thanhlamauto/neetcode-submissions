class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = dict()
        ans = 0

        for right in range(len(s)):
            c = s[right]
            freq[c] = freq.get(c, 0) + 1

            while freq[c] > 1:
                d = s[left]
                freq[d] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        
        return ans 