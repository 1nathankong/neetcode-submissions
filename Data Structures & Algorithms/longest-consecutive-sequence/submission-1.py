class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        put numbers into dictionary

        example: [2,20,4,10,3,4,5]

        into: {'2':1, '20':1, '4':2, '10':1, '3':1, '5':1}
        change al entries into: 
        {'2':1, '20':1, '4':1, '10':1, '3':1, '5':1}
        sort back into list:
        [2,3,4,5,10,20]

        use fast and slower pointer to check each element is one greater than previous 
        and then stop once that is no longer achieved 
        
        return the consecutive element counter
        """
        if not nums:
            return 0
        current = 0
        current_next = current + 1
        
        d = defaultdict(int)
        max_count = 1
        counter = 1
        for i in nums:
            d[i] += 1
        for i in d:
            if d[i] > 1:
                d[i] = 1
        nums_sorted = sorted(list(d))

        while current_next < len(nums_sorted):
            if (nums_sorted[current_next] - nums_sorted[current] == 1):
                
                counter += 1
                current += 1
                current_next += 1

                max_count = max(counter, max_count)

            else:
                counter = 1
                current += 1
                current_next += 1
        
        return max_count

        