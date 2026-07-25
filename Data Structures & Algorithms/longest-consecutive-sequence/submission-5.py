class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = []
        nums.sort()
        ans = 0
        count = 0
        while nums:
            count = 1
            temp = nums.pop(0)
            while temp+1 in nums:
                nums.remove(temp+1)
                count += 1
                temp += 1
            if count > ans: ans = count
        return ans
