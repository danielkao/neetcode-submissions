import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        if len(s) == 1:
            return True
        s = s.replace(" ", "")
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()

        return s == s[::-1]
