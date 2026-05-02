class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + i + '.'
        return s

    def decode(self, s: str) -> List[str]:
        l = s.split('.')
        k=[]
        for i in range(len(l)-1):
            if l[i] != '.':
                k.append(l[i])
        return k