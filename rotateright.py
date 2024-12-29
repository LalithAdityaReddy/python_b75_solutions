nums=([])
n=int(input("enter the no.of array elements"))
for i in range(n):
    k=int(input("enter elements"))
    nums.append(k)
k=int(input("enter how many steps to rotate: "))
nums = nums[-k:] + nums[:-k] 
print(nums)