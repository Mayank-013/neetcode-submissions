class Solution:
    def isValid(self, s: str) -> bool:
        p = ["#"]
        for i in s:
            if i == ")":
                if p[-1] == "(":
                    p.pop()
                    continue
            elif i == "}":
                if p[-1] == "{":
                    p.pop()
                    continue
            elif i == "]":
                if p[-1] == "[":
                    p.pop()
                    continue
            p.append(i)
        return True if p[-1] == "#" else False
            
            
        