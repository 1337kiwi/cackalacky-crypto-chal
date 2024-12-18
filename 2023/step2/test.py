numbers = input("Enter numbers separated by spaces: ").split()

output = []
for num in numbers:
    # Convert the string to an integer
    num = int(num)

    # Get the hundreds, tens, and ones places
    hundreds = (num // 100) * 100
    tens = ((num // 10) % 10) * 10
    ones = num % 10

    # Append the sum of the hundreds, tens, and ones places to the output list
    output.append(f"{hundreds} + {tens} + {ones}")

# Join the output list by | to create a single string
result = " | ".join(output)

# Save the result to a file called "output.txt"
with open("output.txt", "w") as f:
    f.write(result)