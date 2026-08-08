from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            sorted_string = sorted(i)
            str_i = ''.join(sorted_string)
            d[str_i].append(i)
        return list(d.values())        