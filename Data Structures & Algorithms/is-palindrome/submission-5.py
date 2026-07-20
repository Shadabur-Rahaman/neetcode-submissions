class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ''
        for n in s:
            if n.isalnum():
                m += n.lower()
        return m==m[::-1]