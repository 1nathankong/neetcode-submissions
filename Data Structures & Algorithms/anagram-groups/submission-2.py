from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            sorted_s=sorted(i)
            sorted_string = ''.join(sorted_s)
            d[sorted_string].append(i)
        return list(d.values())




        