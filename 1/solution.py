def sum_of_multiples_of_3_and_5(value):
    sum = 0
    for i in range(value):
        if i % 3 == 0 or i % 5 == 0:
            sum += i     
    return sum

if __name__ == "__main__":
    print(sum_of_multiples_of_3_and_5(1000))