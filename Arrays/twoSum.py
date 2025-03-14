## O(n^2)
def twoSum( nums, target) :
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            sum = nums[i] + nums[j]
            if target == sum and i != j:
                return (i, j)
            

## O(n) - Optimized using a dictionary to store compliments
def twoSumOptimized(nums, target) :
    previous_numbers = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in previous_numbers:
            return (previous_numbers[complement], idx)
        previous_numbers[num] = idx


nums = [-3,4,3,90]
target = 0
output = twoSum(nums,target)
print(output)
