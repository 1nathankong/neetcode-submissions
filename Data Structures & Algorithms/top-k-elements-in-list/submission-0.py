class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        lst = []
        common = s.most_common(k)
        for i in common:
            lst.append(i[0])
        return lst