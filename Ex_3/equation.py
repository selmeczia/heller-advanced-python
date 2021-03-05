mapping = {"a": 2, "b": 5, "c": -4, "d": 1}
equation = "a+b+c+d"

result = sum([mapping[value] for value in equation.split("+")])

print(result)
