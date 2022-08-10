class Solution:
    def insert(
        intervals, newInterval
    ):
        res = []

        while True:
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res

print(Solution.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))