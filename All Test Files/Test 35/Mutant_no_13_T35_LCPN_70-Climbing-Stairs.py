class Solution:
    def climbStairs(n: int) -> int:
         
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

print(Solution.climbStairs(n=2))