class Rotate:
    def __init__(self, nums):
        self.nums = nums

    def rotate_list(self):
        count = 0
        for _ in range(len(self.nums)):  # Loop over the number of elements
            if self.nums[0] > self.nums[-1]:  # Check if rotation is needed
                # Perform a single rotation
                self.nums = self.nums[1:] + self.nums[:1]
                count += 1
            else:
                break  # Stop if the list is sorted
        
        print(f"{count} times rotated")
        return self.nums[0]  # Return the first element after rotation


n = Rotate([3, 4, 5, 1, 2])
k = n.rotate_list()  # Call the method correctly
print(k)
