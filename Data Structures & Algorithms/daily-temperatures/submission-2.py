class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        ans = [0] * len(temperatures)
        s = []
        
        for i,j in enumerate(temperatures):
            while s and j > s[-1][1]:
                m,n = s.pop()
                ans[m] = i - m
            s.append([i,j])
            #print(s)
        return ans
        