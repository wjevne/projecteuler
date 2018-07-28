def fibonacci(end):
    prev, cur = 0, 1

    while prev <= end:
        yield prev
        prev, cur = cur, prev + cur
