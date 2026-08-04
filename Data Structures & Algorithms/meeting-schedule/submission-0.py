"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        # 1. Ordenamos las reuniones por la hora de inicio (start)
        intervals.sort(key=lambda i: i.start)

        # 2. Comparamos cada reunión con la siguiente
        for i in range(len(intervals) - 1):
            reunion_actual = intervals[i]
            reunion_siguiente = intervals[i + 1]
            
            if reunion_siguiente.start < reunion_actual.end:
                return False

        # 3. Si recorrimos todas sin solapamientos, se pueden hacer todas
        return True