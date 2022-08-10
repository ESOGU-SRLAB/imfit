class Solution:
    def lengthOfLIS(nums) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                 
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

print(Solution.lengthOfLIS(nums = [7,7,7,7,7,7,7]))