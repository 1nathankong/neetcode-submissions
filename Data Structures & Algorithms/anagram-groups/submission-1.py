class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sorted_i = sorted(i)
            str_i = ''.join(sorted_i)
            if str_i not in d:
                d[str_i] = [i]
            else:
                d[str_i].append(i)
        return list(d.values())        