nums = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    nums.append(value)
out=[]
product=1
for i in range(len(nums)):
    for j in range(len(nums)):
        if i!=j:
            product=product*nums[j]
    out.append(product)
    product=1
print(out)               
