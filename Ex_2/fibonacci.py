
def fibonacci(n: int, cache: list = [1, 1]) -> int:
    print(cache)
    if n <= 1:
        return n
    if n < len(cache):
        return cache[n-1]
    for i in range(len(cache), n):
        cache.append(cache[-1] + cache[-2])
    return cache[n-1]


print(fibonacci(4))
print(fibonacci(6))
print(fibonacci(8))
