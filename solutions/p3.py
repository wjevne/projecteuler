from solutions.utils.factorization import factor


def largest_prime_factor(n):
    return max(factor(n))


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))