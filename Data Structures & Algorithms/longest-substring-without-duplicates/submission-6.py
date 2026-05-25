class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen = dict()

        for r, c in enumerate(s):
            if c in seen:
                l = max(seen[c] + 1, l) # using max prevents us from moving l to a lower position than the ones it's already at
            res = max(res, r - l + 1)
            seen[c] = r
        
        return res
