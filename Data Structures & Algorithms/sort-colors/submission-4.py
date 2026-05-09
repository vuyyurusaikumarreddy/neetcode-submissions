class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0:0,1:0,2:0}
        for i in nums:
            d[i] += 1
        i = 0
        for k in list(d.keys()):
            print(k,d[k])
            for j in range(d[k]):
                nums[i] = k
                i = i + 1
            