class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


sol = Solution()
nums = [1, 2, 3, 2, 1]
sol.containsDuplicate(nums)
