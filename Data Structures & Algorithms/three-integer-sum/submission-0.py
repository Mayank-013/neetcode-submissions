class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a= []
        

        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if -nums[i] - nums[j] in nums[j+1:]:
                    b = [nums[i],nums[j],-nums[i]-nums[j]]
                    b.sort()
                    if b not in a:
                        a.append(b)
        
        return a