class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        store freq values into list:
        lst = []
        turn into dictionary: 
        
        example:
        nums = [1,2,2,3,3,3], k = 2
        {1: 1, 2: 2, 3: 3}

        decrement = k

        find first key with highest value:
        which is 3. 
        append 3: [3]
        k = 1
        delete 3:
        {1: 1, 2: 2}

        repeat process again:
        2 is key with highest value
        append 2: [3,2]
        delete 2
        k = 0

        return list [3,2]
        """
        lst = []
        if not nums or k == 0:
            return 0

        sorted_nums = sorted(nums)
        d = defaultdict(int)

        for i in sorted_nums:
            d[i] += 1
        print(d)

        decrement = k
        while decrement > 0:
            max_key = max(d, key=d.get)
            lst.append(int(max_key))
            del d[max_key]
            decrement -= 1
        return lst
