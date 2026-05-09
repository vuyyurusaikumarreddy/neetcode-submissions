class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0:0,1:0,2:0}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        i = 0
        while i < len(nums):
            for j in range(d[0]):
                nums[i] = 0
                i = i + 1
            for j in range(d[1]):
                nums[i] = 1
                i = i + 1
            for j in range(d[2]):
                nums[i] = 2
                i = i + 1
            