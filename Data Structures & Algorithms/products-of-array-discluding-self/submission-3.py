class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = 1
        zero_count = 0

        for i in nums:
            if i != 0:
                r *= i
            else:
                zero_count += 1

        res = []
        for i in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if i == 0:
                    res.append(r)
                else:
                    res.append(0)
            else:
                res.append(r // i)

        return res