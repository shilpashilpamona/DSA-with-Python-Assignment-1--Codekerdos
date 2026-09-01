def twoSum(nums, target):

    seen = {}

    for i in range(len(nums)):

        current = nums[i]
        required = target - current

        if required in seen:
            return [seen[required], i]

        seen[current] = i

    return []
