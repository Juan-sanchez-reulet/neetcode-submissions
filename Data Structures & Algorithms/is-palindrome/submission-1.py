class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        if not s:
            return True
        first,last=0,len(s)-1
        while first < last:
            if s[first]!=s[last]:
                return False
            first+=1
            last-=1
        return True