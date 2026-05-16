class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_s = {}
        for i in range(len(s)):
            char_count_s[s[i]] = char_count_s.get(s[i],0) + 1
            char_count_s[t[i]] = char_count_s.get(t[i],0) - 1
        return all(v == 0 for v in char_count_s.values())