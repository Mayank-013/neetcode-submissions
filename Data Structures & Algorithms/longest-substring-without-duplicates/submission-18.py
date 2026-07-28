class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)):
            l = i
            r = i
            temp = [s[i]]
            while l > 0 or r < len(s)-1:
                if l > 0: l -= 1
                if r < len(s)-1: r += 1
                if s[l] not in temp:
                    temp.append(s[l]) 
                else:
                    break
                if s[r] not in temp:
                    temp.append(s[r]) 
                else: 
                    break
            max = len(temp) if len(temp) > max else max
            print(temp)
        return max

                
            