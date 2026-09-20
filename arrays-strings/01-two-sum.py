def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


# Test input
nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)

print("Output:", result)