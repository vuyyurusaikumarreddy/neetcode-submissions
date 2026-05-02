class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        j = 0
        n = min(len(s) for s in strs)
        s = ""
        
        while i < n:
            j = 0
            k = strs[j][i]
            while j < len(strs):
                if strs[j][i] != k:
                    return s
                j = j + 1
            i = i + 1
            s = s + k
        return s