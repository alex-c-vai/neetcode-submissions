class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 0
        while i < n:
            if i < n-1 and intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [intervals[i][0], max(intervals[i][1],intervals[i+1][1])]
                intervals[i] = None
            i += 1
        
        return [interval for interval in intervals if interval != None]