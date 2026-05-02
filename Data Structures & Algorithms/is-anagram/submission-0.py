class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # st = {}
        # for i in s:
        #     if t in st:
        #         st[i] = st[i] + 1
        #     else:
        #         st[i] = 1
        # for i in t:
        #     if t in tt:
        #         tt[i] = tt[i] + 1
        #     else:
        #         tt[i] = 1
        return "".join(sorted(s)) == "".join(sorted(t))
        