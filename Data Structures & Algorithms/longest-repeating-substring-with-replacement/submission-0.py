from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            charCount[s[r]] += 1
            maxf = max(maxf, charCount[s[r]])
            if r-l+1 - maxf > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
            
        return res
                