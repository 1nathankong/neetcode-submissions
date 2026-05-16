import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        idx1 = 0
        idx2 = len(s) - 1 

        while idx1 < idx2:
            print("idx1", s[idx1])
            print("idx2", s[idx2])
            if s[idx1] != s[idx2]:
                return False
            idx1 += 1
            idx2 -= 1
        return True
        
        