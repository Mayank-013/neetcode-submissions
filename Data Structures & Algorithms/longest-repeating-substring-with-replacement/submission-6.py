from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        visited = []
        change = 0
        for i in s:
            visited.append(i)
            t = dict(Counter(visited))
            if len(visited) - Counter(visited).most_common(1)[0][1] > k:
                print("triggered")
                count = len(visited)-1 if len(visited) > count else count
                visited.pop(0)
            

        return len(visited) if len(visited) > count else count
                

                
        