class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.lower() if char.isalnum()]
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
