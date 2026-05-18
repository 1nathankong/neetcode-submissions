class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            '}': '{',
            ')':'(',
            ']':'['
        }

        for char in s:
            if char in '[{(':
                stack.append(char)
            elif stack == []:
                return False
            elif matches[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return stack == []





        