#Generate list of numbers that satisfies condition of being divisible by 3, where its root is an integer in the range of 1-100

list1 = [x**2 for x in range(1,101) if x**2%3 == 0]

print(list1)