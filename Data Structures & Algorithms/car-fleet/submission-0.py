class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        idx = sorted(range(len(position)), key=lambda i: position[i])
        fleet = previous_time = 0

        for i in idx[::-1]:
            t = (target - position[i]) / speed[i]
            if t > previous_time:
                fleet += 1
                previous_time = t
        return fleet