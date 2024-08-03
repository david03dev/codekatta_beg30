# Read input
num = int(input().strip())

# Calculate the sum of digits
digit_sum = sum(int(digit) for digit in str(abs(num)))

# Print the result
print(digit_sum)
