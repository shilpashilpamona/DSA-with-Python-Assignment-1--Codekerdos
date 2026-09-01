class Solution(object):
    def max_subarray(self, nums, k):
        win_sum = sum(nums[:k])
        max_sum = win_sum

        for i in range(k, len(nums)):
            updated_sum = max_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, updated_sum)

        return max_sum / k


sol = Solution()
nums = [0, -2, -4, 8, 3, -3]
k = 4
sol.max_subarray(nums, k)
print(sol.max_subarray(nums, k))
