def equation(string_imput, *args, **kwargs) -> int:
    """
    The function calculates the equation from a string. Returns at integer.
    """

    result = int()

    for arg in args:
        result += arg
    for key, value in kwargs.items():
        result += value

    return result


print(equation("a+b+c", 1, -2, 7))
