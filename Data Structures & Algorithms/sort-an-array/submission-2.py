class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def divide(nums):
            if len(nums) <= 1:
                return nums
            m = len(nums)//2
            l = divide(nums[:m])
            r = divide(nums[m:])
            return merge(l,r)
        def merge(l,r):
            i = 0
            j = 0
            m=[]
            while(i<len(l) and j < len(r)):
                if l[i] < r[j]:
                    m.append(l[i])
                    i = i + 1
                else:
                    m.append(r[j])
                    j = j + 1
            if i < len(l):
                m.extend(l[i:])
            if j < len(r):
                m.extend(r[j:])
            return m
        return divide(nums)