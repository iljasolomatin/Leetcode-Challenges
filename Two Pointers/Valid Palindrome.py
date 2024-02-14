class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        
        for a in list(s):
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])