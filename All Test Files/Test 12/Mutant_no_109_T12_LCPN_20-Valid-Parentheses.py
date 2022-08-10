class Solution:
    def isValid(s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return returnFalse
            stack.pop()

        return not stack

print(Solution.isValid(s = "()"))