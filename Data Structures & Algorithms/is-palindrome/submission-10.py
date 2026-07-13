class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()
        while end > start:
            left = s[start]
            right = s[end]
            if not left.isalnum():
                start += 1
                continue
            if not right.isalnum():
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        return True