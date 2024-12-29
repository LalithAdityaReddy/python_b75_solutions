nums = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    nums.append(value)

# Check for consecutive duplicates
flag = False
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        flag = True
        break

# Output the result
print(flag)


        
       