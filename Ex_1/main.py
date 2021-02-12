# creating numbers into list from 1 to 100
numbers = list(range(1, 100))
# creating empty list
num_3 = list()
# for cycle for every number divisible by 3
for num in numbers:
    if num % 3 == 0: num_3.append(num)
# print return
print(num_3)