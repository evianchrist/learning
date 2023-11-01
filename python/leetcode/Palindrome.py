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
        
# this was very slow compared to most users

# new better solution below
# key is isalnum function

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s.lower():
            if i.isalnum():
                s1 += i

        if s1 == s1[::-1]:
            return True
        else:
            return False