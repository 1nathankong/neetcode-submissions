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

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append((t,i))
        return answer
        





        


        