class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for i in s.lower():
            if i.isalnum():
                p += i
        if p == p[-1::-1]: return True
        return False
