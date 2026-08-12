class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0

        for i in nums:
            if i == 0:
                zeroes += 1
            else:
                product *= i
        if zeroes > 1 :
            return [0]*len(nums)

        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zeroes:
                if c != 0:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product // c

        return res
