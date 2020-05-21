# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        intervals.sort(key = lambda i:i.start)
        result.append(intervals[0])
        for element in intervals:
            if result[-1].end < element.start:
                result.append(element)
            else:
                result[-1].end = max(result[-1].end, element.end)
        return result
    
    