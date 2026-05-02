class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            if sort in d:
                d[sort].append(strs[i])
            else:
                d[sort] = [strs[i]]
        return list(d.values())