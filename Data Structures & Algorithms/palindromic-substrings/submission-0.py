class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expand(l, r, s):
            nonlocal res
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1 # we are not looking for unique palindromes
                l -= 1
                r += 1
            return
        
        for i in range(len(s)):
            expand(i, i, s)
            expand(i, i+1, s)
        return res