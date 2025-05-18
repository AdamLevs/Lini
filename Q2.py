# All the inputs must be integers and positive

# Section 1
n = int(input("Please enter a number: "))
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(f"Divisors of {n} are: {divisors}")

# Section 2
n = int(input("Please enter a number to check if it's prime: "))
find_divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        find_divisors.append(i)

is_prime = len(find_divisors) == 2
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

# Section 3
limit = int(input("Please enter a limit: "))
file = open('composite_numbers.txt', 'w')
for num in range(2, limit + 1):
    num_divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            num_divisors.append(i)

    is_not_prime = len(num_divisors) != 2
    has_less_than_10_divisors = len(num_divisors) < 10

    if is_not_prime and has_less_than_10_divisors:
        file.write(str(num) + '\n')

file.close()
