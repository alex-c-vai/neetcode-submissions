class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(l, r, s):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i,i,s)
            even = expandAroundCenter(i, i+1, s)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        
        return res