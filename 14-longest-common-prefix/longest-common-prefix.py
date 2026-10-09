class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min=float("inf")
        for s in strs:
            if len(s)<min:
                min=len(s)
        i=0
        while i<min:
            for s in strs:
                if s[i]!= strs[0][i]:
                    return s[:i]
            i+=1
        return s[:i]