class Solution:
    def uniquePaths(m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
             
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)

print(Solution.uniquePaths(m = 3, n = 7))