from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        k = Counter(t)
        ck = {}
        nd = len(k)
        hv = 0

        l = 0
        ans = [-1, -1]
        mn = float("inf")

        for r in range(len(s)):
            c = s[r]

            if c in k:
                ck[c] = ck.get(c, 0) + 1

                if ck[c] == k[c]:
                    hv += 1

            while hv == nd:
                if r - l + 1 < mn:
                    mn = r - l + 1
                    ans = [l, r]

                c = s[l]

                if c in k:
                    if ck[c] == k[c]:
                        hv -= 1

                    ck[c] -= 1

                l += 1

        l, r = ans

        return "" if l == -1 else s[l:r+1]