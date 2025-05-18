# Change the lists if needed for testing
# The question don't say that the user should input the lists!
# The numbers must be integers, the question don't say that they must be positive!
# But we will assume that they are.

# section 1
listanalyse = [3, 5, 7, 2, 8]

if len(listanalyse) > 0:
    minimum = min(listanalyse)
    maximum = max(listanalyse)
    average = sum(listanalyse) / len(listanalyse)
    result = [minimum, maximum, average]
    print(f"[min, max, avg]: {result}")
else:
    print("Please enter at least 1 number inside the list")

print("-----------------------------------------------")

# section 2
even_odd_analysis = [1, 2, 3, 4, 5]

even_count = 0
odd_count = 0
even_sum = 0

for num in even_odd_analysis:
    if num % 2 == 0:
        even_count += 1
        even_sum += num
    else:
        odd_count += 1

if even_count > 0:
    even_average = even_sum / even_count
else:
    even_average = 0

result = [even_count, odd_count, even_average]

print(f"[even_count, odd_count, even_avg]: {result}")
