class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # r = 1
        # zero_count = 0

        # for i in nums:
        #     if i != 0:
        #         r *= i
        #     else:
        #         zero_count += 1

        # res = []
        # for i in nums:
        #     if zero_count > 1:
        #         res.append(0)
        #     elif zero_count == 1:
        #         if i == 0:
        #             res.append(r)
        #         else:
        #             res.append(0)
        #     else:
        #         res.append(r // i)

        # return res

        l = [1]*len(nums)
        p=nums[0]
        for i in range(1, len(nums)):
            l[i]=p
            p = p * nums[i]
        print(l)
        i=len(nums)-1
        p = 1
        while i>=0:
            l[i]=p*l[i]
            p = p * nums[i]
            i = i - 1
        return l




