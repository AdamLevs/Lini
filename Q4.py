# Change the lists if needed for testing
# The question don't say that the user should input the lists!
# The lists length must be the same.
list1 = [4, 7, 9]
list2 = [1, 3, 5]

if len(list1) != len(list2):
    print("Lists with not the same length!")
else:
    result = 0
    for i in range(len(list1)):
        scalar_product = list1[i] * list2[i]
        result += scalar_product

    print(result)
