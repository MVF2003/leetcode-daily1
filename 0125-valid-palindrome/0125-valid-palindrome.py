class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        if s[::-1].lower() == s.lower():
            return True
        else: 
            return False