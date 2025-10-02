#Challenge 1
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")
while current_number != 1:
    print(current_number, end=" ")

    if current_number % 2 == 0:
        current_number //= 2
    else:
        current_number = current_number * 3 + 1

    step_count += 1

print(1)
print(f"Steps: {step_count}")

#Challenge 2
print("\n=== Challenge 2: Prime Number Checker ===")

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not prime (must be greater than 1).")
else:
    print(f"Testing divisors from 2 to {num - 1}...")

    is_prime = True


    for divisor in range(2, num):
        if num % divisor == 0:
            print(f"{num} is not prime (divisible by {divisor})")
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime!")
#Challenge 3
print("\n=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# Print header row
print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Outer loop for rows (1–10)
for row in range(1, 11):
    # Print row number at start of line
    print(f"{row:2} ", end="")

    # Inner loop for columns (1–10)
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")

    print()  # New line after each row
