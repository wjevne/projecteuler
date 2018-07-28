from utils.fibonacci import fibonacci


def sum_of_even_fibonacci(value):
    res = 0

    for i in fibonacci(value):
        if i % 2 == 0:
            res += i

    return res

if __name__ == "__main__":
    print(sum_of_even_fibonacci(4e6))
