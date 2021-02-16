import random
from multiprocessing import Pool, cpu_count


def pi_approx(n: int) -> float:
    x_list = []
    y_list = []
    hit = 0
    miss = 0

    for i in range(0, n):
        temp = random.random()
        x_list.append(temp)

    for j in range(0, n):
        temp_2 = random.random()
        y_list.append(temp_2)

    for a, b in zip(x_list, y_list):

        if (a**2 + b**2)**0.5 < 1:
            hit = hit + 1
        else:
            miss = miss + 1

    pi = hit / n * 4
    print(f'With {n} iterations the pi value is : {pi}')


def main():
    print(f'Starting calculating pi on {cpu_count()} cores...')
    number_of_iterations = 1000000

    with Pool() as pool:
        pi_approx(number_of_iterations)


if __name__ == '__main__':
    main()
