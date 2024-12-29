nums = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    nums.append(value)

# Initialize variables
max_sum = nums[0]  # Maximum subarray sum found so far
current_sum = nums[0]  # Current subarray sum

# Traverse the array
for i in range(1, len(nums)):
    # Update current_sum to include the current element or start a new subarray
    current_sum = max(nums[i], current_sum + nums[i])
    # Update max_sum if current_sum is greater
    max_sum = max(max_sum, current_sum)

print("Maximum subarray sum is:", max_sum)
