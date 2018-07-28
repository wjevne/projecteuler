def sum_of_multiples_of_3_and_5(value):
    res = 0

    for i in range(value):
        if i % 3 == 0 or i % 5 == 0:
            res += i

    return res

if __name__ == "__main__":
    print(sum_of_multiples_of_3_and_5(1000))
