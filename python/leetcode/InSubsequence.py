class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        found = 0
        if len(t) < len(s):
            return False

        for count, i in enumerate(s):
            found = 0
            while found == 0:
                if i == t[k]:
                    found = 1
                k += 1
                if k >= len(t) and found == 0:
                    return False
                if k >= len(t) and count < (len(s)-1):
                    return False
        return True
                