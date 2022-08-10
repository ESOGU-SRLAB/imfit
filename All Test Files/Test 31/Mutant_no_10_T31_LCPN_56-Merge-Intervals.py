class Solution:
    def merge(intervals):
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        while True:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

print(Solution.merge(intervals = [[1,4],[4,5]]))