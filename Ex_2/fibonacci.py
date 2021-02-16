
def fibonacci(n: int, cache: list = [1, 1, 2, 3, 5, 8]) -> int:
    if n <= 1:
        return n
    if n <= len(cache):
        return cache[n-1]
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))

