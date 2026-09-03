class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i,j in enumerate(position):
            position[i] = [j,(target - position[i])/speed[i]]
        position = sorted(position, key = lambda x: x[0], reverse=True)
        #print(position)
        fleet = 1
    
        m = position[0][1]
        for i in position[1:]:
            if i[1] > m:
                fleet+=1
                m = i[1]
        
        return fleet