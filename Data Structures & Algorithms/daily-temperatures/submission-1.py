class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        do something with push and popping

        1. push idx into stack
        2. if next idx greater than it pop and store count in list
        3. keep repeating until end of list
        """
        answer = [0] * len(temperatures)
        stack = []

        for j in range(len(temperatures)):
            temp = temperatures[j]
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                answer[i] = j-i
            stack.append(j)
        return answer

        





        


        