prices = []
n = int(input("Enter number of days: "))
for i in range(n):
    value = int(input(f"Enter price for day {i+1}: "))
    prices.append(value)

# Initialize variables
low = prices[0]
low_pos = 0
high = 0
high_pos = 0

# Find the lowest price and its position
for i in range(len(prices)):
    if prices[i] < low:
        low = prices[i]
        low_pos = i

# Find the highest price after the lowest price
high = low  # Start from the lowest price
for j in range(low_pos + 1, len(prices)):
    if prices[j] > high:
        high = prices[j]
        high_pos = j

# Output the results
if high_pos > low_pos:
    print("Maximum profit is", high - low, "!")
    print("Buy on day", low_pos + 1, "and sell on day", high_pos + 1)
else:
    print("No profit can be made.")

