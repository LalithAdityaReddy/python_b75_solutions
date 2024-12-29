n = int(input("Enter the number of values: "))
nums = []
target = int(input("Enter target value: "))
for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    nums.append(value)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] + nums[i] == target:
            print(f"Pair found at indices {i} and {j}: ({nums[i]}, {nums[j]})")
