class Solution(object):
    def sq_sorted_array(self, nums):
        n = len(nums)
        answer = [0] * n

        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):

            if abs(nums[left]) > abs(nums[right]):
                answer[i] = nums[left] ** 2
                left += 1

            else:
                answer[i] = nums[right] ** 2
                right -= 1

        return answer


sol = Solution()
nums = [-2, -1, 0, 3, 5, 8, 9]
k = 4
sol.sq_sorted_array(nums)
print(sol.sq_sorted_array(nums))
