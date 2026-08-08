from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str not in d:
                d[sorted_str] = [i]
            else:
                d[sorted_str].append(i)
        return [value for value in d.values()]       



        