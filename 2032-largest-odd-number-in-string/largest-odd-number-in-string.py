class Solution:
    def largestOddNumber(self, s: str) -> str:
        i=len(s)-1
        while i>=0:
            if int(s[i])%2!=0:
                ans=s[:i+1]
                return ans.lstrip('0')
            i-=1
        return ''
        