class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = 0
        prod = 1
        for i in nums:
            if i == 0: num +=1
            else: prod *= i
        if num > 1: return [0] * len(nums)
        if num == 0: return [prod//i for i in nums]
        a = []
        for i in nums:
            if i == 0:
                a.append(prod)
            else: a.append(0)
        return a
        