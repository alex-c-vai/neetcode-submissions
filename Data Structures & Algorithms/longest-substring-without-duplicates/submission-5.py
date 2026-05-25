class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen = dict()

        for r, c in enumerate(s):
            if c in seen:
                l = max(seen[c] + 1, l)
            res = max(res, r - l + 1)
            seen[c] = r
        
        return res
