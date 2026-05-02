"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        i=0
        while i < len(intervals)-1:
            print(intervals[i].start<intervals[i+1].start)
            print(intervals[i].end<intervals[i+1].end)
            if intervals[i+1].start<intervals[i].end:
                return False
            i = i + 1
        
        return True
