class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(2*len(nums))]
        i = 0
        j = 0
        while i < len(ans):
            ans[i] = nums[j]
            j = j + 1
            if i == len(nums)-1:
                j = 0
            i = i + 1
        print(ans)
        return ans
