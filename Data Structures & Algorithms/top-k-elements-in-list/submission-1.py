class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        sd = dict(sorted(d.items(), key=lambda i: i[1], reverse=True))
        return list(sd.keys())[:k]
