class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            else:
                freq[nums[i]] = 1

        return False


sol = Solution()
nums = [1, 2, 3, 2, 1]
sol.containsDuplicate(nums)
