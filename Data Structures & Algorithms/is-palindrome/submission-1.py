import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
           return True
        # NAIVE:
        # if len(s) == 1:
        #     return True
        # s = s.replace(" ", "")
        # s = re.sub("[^a-zA-Z0-9]", "", s).lower()

        # return s == s[::-1]

        i, j = 0, len(s) - 1

        while j > i:

            while j > i and not s[j].isalnum():
                j -= 1
            while j > i and not s[i].isalnum():
                i += 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True