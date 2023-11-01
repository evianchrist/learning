class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""
        s = s.lower()
        for i in s:
            if (48 <= ord(i) <= 57) or (97 <= ord(i) <= 122):
                output = output + i
        s = output
        output = s[::-1]

        if s == output:
            return True
        else:
            return False
        
