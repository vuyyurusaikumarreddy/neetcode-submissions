class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(x)) for x in strs]
        d = {}
        for i in range(len(sorted_strs)):
            if sorted_strs[i] in d:
                d[sorted_strs[i]].append(strs[i])
            else:
                d[sorted_strs[i]] = [strs[i]]
        return list(d.values())