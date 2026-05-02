class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            c = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            d[c] = i
        return [1,1]