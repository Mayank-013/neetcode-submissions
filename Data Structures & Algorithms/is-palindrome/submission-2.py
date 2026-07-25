class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for i in s:
            if i.isalnum():
                p += i.lower()
        if p == p[-1::-1]: return True
        return False
