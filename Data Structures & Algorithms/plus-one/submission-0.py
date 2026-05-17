class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in digits:
            result = "".join(str(item) for item in digits)
        result = int(result)
        result += 1
        res = [int(digit) for digit in str(result)]
        return res


        