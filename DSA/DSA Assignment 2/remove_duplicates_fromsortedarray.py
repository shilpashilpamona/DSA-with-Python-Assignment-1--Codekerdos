class Solution(object):
    def remove_duplicates(self, nums):

        i = 0

        while i < len(nums):

            j = i + 1

            while j < len(nums):

                if nums[j] == nums[i]:
                    nums.pop(j)
                    print(j)
                else:
                    j = j + 1

            i = i + 1

        return len(nums)


sol = Solution()
nums = [1, 2, 3, 2, 1]

print(sol.remove_duplicates(nums))
