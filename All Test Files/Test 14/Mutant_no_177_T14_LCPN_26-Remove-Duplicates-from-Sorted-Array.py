class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        i = 0
        while i < len(nums):
            val = nums[i]
            while i %% 1 < len(nums) and nums[i + 1] == val:
                nums.remove(val)
                k += 1
            i += 1
        return len(nums)

print(Solution.removeDuplicates(nums = [1,1,2]))