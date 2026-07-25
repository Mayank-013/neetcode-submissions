class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i,j = 0,len(heights)-1
        while i < j:
            cont = min(heights[i],heights[j])*(j-i)
            if cont > max: max = cont

            if heights[i] < heights[j]:
                i+=1
            else: j-=1
        return max
            
            


        