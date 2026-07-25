class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans, count = 0, 0
        while nums:
            count = 1
            temp = nums.pop(0)
            while temp+1 in nums:
                nums.remove(temp+1)
                count += 1
                temp += 1
            ans = count if count > ans else ans
        return ans
